__pdoc__ = {}
for func_name in [
    "boot",
    "cleanup",
    "get_parameter",
    "load_test_parameters",
    "write_result_to_db",
    "tmp_dir",
    "tmp_filepath",
    "RESULT_FILENAME",
    "load_result"
]:
    __pdoc__[f"app.Application.{func_name}"] = False
__pdoc__["config"] = False
__pdoc__["db_cache"] = False
__pdoc__["db_models"] = False