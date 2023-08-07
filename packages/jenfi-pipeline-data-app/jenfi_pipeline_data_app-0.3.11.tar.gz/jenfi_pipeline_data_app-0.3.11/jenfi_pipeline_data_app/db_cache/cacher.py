import boto3
import pickle
import hashlib
import logging
import sqlparse

from pathlib import Path
from functools import lru_cache


class Cacher(object):
    MAX_NORMALIZE_QUERY_LENGTH = 40000
    LOGGER = logging.getLogger(__name__)

    def __init__(
        self,
        logical_step_name: str,
        state_machine_run_id: str,
        local_cache_dir: Path,
        s3_bucket_name: str,
    ) -> None:
        self.logical_step_name = logical_step_name
        self.state_machine_run_id = state_machine_run_id

        self.local_cache_dir = local_cache_dir
        self.s3_cache_bucket_name = s3_bucket_name

        pass

    def from_cache(self, query_str):
        if self._local_filepath(query_str).is_file():
            self.LOGGER.debug("LOCAL CACHE")
            with open(self._local_filepath(query_str), "rb") as f:
                return pickle.load(f)
        else:
            # download _cache_key from S3
            result = self._load_from_s3(query_str)

            # save the cache locally
            self._save_locally(query_str, result)

            # unseralize
            return result

    def to_cache(self, query_str, result):
        self._save_to_s3(query_str, result)
        self._save_locally(query_str, result)

        pass

    def exists(self, query_str):
        """
        This only checks if it exists on S3 as source of truth.

        Doesn't matter if it exists locally. That's just to help speed.
        """

        from botocore.errorfactory import ClientError

        filepath = self._filename(query_str)
        s3 = boto3.client("s3")

        try:
            s3.head_object(Bucket=self.s3_cache_bucket_name, Key=filepath)

            return True
        except ClientError:
            # Not found
            return False

    def _local_filepath(self, query_str) -> Path:
        filename = self._filename(query_str)

        self.local_cache_dir.mkdir(parents=True, exist_ok=True)

        return Path(f"{self.local_cache_dir}/{filename}")

    def _save_to_s3(self, query_str, result):
        pickle_byte_obj = pickle.dumps(result)

        # cache_key from normalizer(query_str), step_name, run_id
        s3_obj = self._s3_cache_obj(query_str)
        s3_obj.put(Body=pickle_byte_obj)

        pass

    def _load_from_s3(self, query_str):
        s3_obj = self._s3_cache_obj(query_str)

        return pickle.loads(s3_obj.get()["Body"].read())

    def _save_locally(self, query_str, result):
        with open(self._local_filepath(query_str), "wb") as f:
            pickle.dump(result, f)

        pass

    def _cache_key(self, query_str):
        # normalize_
        normalized_query = self._normalize(query_str)
        unhashed_key = (
            f"{self.logical_step_name}_{self.state_machine_run_id}_{normalized_query}"
        )

        return self._hash_str(unhashed_key)

    @lru_cache(maxsize=1024)
    def _normalize(self, query_str):
        if len(query_str) > self.MAX_NORMALIZE_QUERY_LENGTH:
            self.LOGGER.debug(
                "The query is too big and would take too much time to normalize. Sending the query as is"
            )
            return query_str
        else:
            return sqlparse.format(
                query_str.strip(),
                reindent=True,
                indent_tabs=False,
                indent_width=4,
                keyword_case="upper",
                strip_comments=True,
            )

    def _hash_str(self, unhashed_key):
        return hashlib.sha1(unhashed_key.encode()).hexdigest()

    def _filename(self, query_str):
        cache_key = self._cache_key(query_str)

        return f"{cache_key}.pickle"

    def _s3_cache_obj(self, query_str):
        filepath = self._filename(query_str)

        s3 = boto3.resource("s3")

        return s3.Object(self.s3_cache_bucket_name, filepath)
