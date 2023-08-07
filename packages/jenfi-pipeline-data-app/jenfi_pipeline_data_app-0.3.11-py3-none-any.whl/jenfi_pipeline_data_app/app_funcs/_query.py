from ..db_cache import DbCache
from pandas import DataFrame

# Primary use point for Credit
# Should be able to help take snapshot of data and return the cache as necessary.
def df_query(self, query_str: str, rebuild_cache: bool=False, skip_cache: bool=False) -> DataFrame:
    """
    Provide a valid psql query_str and returns a Pandas DataFrame. Has caching.
    """
    db_cache = self._db_cache()

    return db_cache.df_query(query_str, rebuild_cache, skip_cache)

# Alias for df_query
query_df = df_query

def query_one(self, query_str: str, rebuild_cache: bool=False, skip_cache: bool=False):
    """
    Direct sqlalchmey fetchone(). Returns None or a dict. Has caching.
    """
    db_cache = self._db_cache()

    return db_cache.query_one(query_str, rebuild_cache, skip_cache)


def query_all(self, query_str: str, rebuild_cache: bool=False, skip_cache: bool=False):
    """
    Direct sqlalchmey fetchall(). Returns an Array. Has caching.
    """

    db_cache = self._db_cache()

    return db_cache.query_all(query_str, rebuild_cache, skip_cache)


def _db_cache(self) -> None:
    (step_name, run_id) = self._run_data()
    bucket_name = self.s3_config.S3_DB_QUERY_CACHE_BUCKET

    return DbCache(
        self.db, self.db_engine, step_name, run_id, self.tmp_dir(), bucket_name
    )
