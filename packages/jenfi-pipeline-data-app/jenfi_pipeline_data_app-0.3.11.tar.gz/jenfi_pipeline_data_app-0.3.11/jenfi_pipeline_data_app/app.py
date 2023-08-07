import sys
import os
import platform
import tempfile
from pathlib import Path

import sklearn


class Application(object):
    """
    .. include:: API.md

    """

    from .app_funcs._constants import (
        ROOT_DIR,
        RESULT_FILENAME,
        PYTHON_ENV,
        STATUS_NOT_APPLICABLE,
        STATUS_INSUFFICIENT_DATA,
        STATUS_SUCCESS,
        STATUS_NO_RESULT,
        STATUS_NOTEBOOK_NOT_FOUND_S3,
    )

    from .app_funcs._db_handler import _init_db, _close_db, _db_config
    from .app_funcs._query import df_query, query_one, query_all, _db_cache
    from .app_funcs._parameters import load_test_parameters, get_parameter, _run_data
    from .app_funcs._result import (
        write_result_to_db,
        write_result,
        load_result,
        _add_run_metadata,
        _remove_results_tmpfile,
        _results_to_tmpfile,
    )
    from .app_funcs._models_s3 import (
        push_model_to_s3,
        load_model_from_s3,
        _init_config_s3,
    )
    from .app_funcs._exit_program import (
        exit_not_applicable,
        exit_insufficient_data,
        notebook_not_found_s3,
    )

    def boot(self):
        """Sets up configs, db connections. It is run as part of the module import."""
        self._init_db()
        self._init_config_s3()
        self._remove_results_tmpfile()  # Any lingering files

    def cleanup(self):
        """Closes connections and cleans up any lingering items."""
        self._close_db()
        self._remove_results_tmpfile()

    def tmp_dir(self) -> Path:
        if self.PYTHON_ENV == "production":
            tmp_path = "/tmp"
        elif self.PYTHON_ENV == "staging":
            tmp_path = "/tmp"
        else:
            tmp_path = (
                "/tmp" if platform.system() == "Darwin" else tempfile.gettempdir()
            )

        return Path(tmp_path)

    def tmp_filepath(self, rel_filepath) -> Path:
        tmp_path = self.tmp_dir()

        return Path(os.path.join(tmp_path, rel_filepath))

    def __repr__(self):
        return self.__dict__

    if "pytest" in sys.modules:
        from .app_funcs._test_funcs import (
            _test_direct_module,
            _test_access_global_var,
            _test_set_global_var,
        )
