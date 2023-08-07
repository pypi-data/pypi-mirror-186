import os
import json
import numpy as np
import pandas as pd

from decimal import Decimal
from datetime import date, datetime
from pathlib import Path


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()

        return super(NpEncoder, self).default(obj)

    def _preprocess_nan(self, obj):
        if isinstance(obj, float) and np.isnan(obj):
            return None
        elif isinstance(obj, dict):
            return {
                self._preprocess_nan(k): self._preprocess_nan(v) for k, v in obj.items()
            }
        elif isinstance(obj, list):
            return [self._preprocess_nan(i) for i in obj]
        return obj

    def iterencode(self, obj):
        return super(NpEncoder, self).iterencode(self._preprocess_nan(obj))


def write_result_to_db(self, logical_step_name, state_machine_run_id, results):
    from ..db_models import state_machine_run_model

    StateMachineRun = state_machine_run_model(self)
    return StateMachineRun().result_to_db(
        logical_step_name, state_machine_run_id, results
    )


def write_result(self, result: dict) -> Path:
    """
    Use after whole notebook is finished to return the final result with a status of `success`
    """

    result_with_metadata = self._add_run_metadata(self.STATUS_SUCCESS, result)

    return self._results_to_tmpfile(result_with_metadata)


def load_result(self):
    result_filepath = self.tmp_filepath(self.RESULT_FILENAME)

    if result_filepath.is_file():
        with open(result_filepath, "r") as result:
            output_data = json.load(result)

        return output_data
    else:
        return self._add_run_metadata(
            self.STATUS_NO_RESULT,
            message="There was no result directly returned from this notebook. Is this expected?",
        )


def _add_run_metadata(
    self, status: str, result: dict = None, message: str = None
) -> dict:
    result_with_metadata = {"run_metadata": {"status": status}}

    if result is not None:
        result_with_metadata = result_with_metadata | result

    if message is not None:
        result_with_metadata["run_metadata"]["message"] = message

    return result_with_metadata


def _results_to_tmpfile(self, result: dict) -> Path:
    result_filepath = self.tmp_filepath(self.RESULT_FILENAME)

    with open(result_filepath, "w") as f:
        json.dump(result, f, cls=NpEncoder)

    return result_filepath


def _remove_results_tmpfile(self) -> None:
    result_filepath = self.tmp_filepath(self.RESULT_FILENAME)

    if result_filepath.is_file():
        os.remove(result_filepath)

    pass
