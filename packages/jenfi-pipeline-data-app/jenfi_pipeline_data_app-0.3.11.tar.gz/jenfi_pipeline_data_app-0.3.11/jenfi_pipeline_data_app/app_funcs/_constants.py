import os

ROOT_DIR = os.path.abspath(os.curdir)
RESULT_FILENAME = "output.json"
PYTHON_ENV = os.getenv("PYTHON_ENV", "development")

STATUS_SUCCESS = "success"
STATUS_NO_RESULT = "no_result_returned"
STATUS_NOT_APPLICABLE = "not_appliciable"
STATUS_INSUFFICIENT_DATA = "insufficient_data"
STATUS_NOTEBOOK_NOT_FOUND_S3 = "notebook_not_found_s3"