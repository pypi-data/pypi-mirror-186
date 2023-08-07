# Exit program
import sys


def exit_not_applicable(self, message: str) -> None:
    """Exits the program early and puts status `not_applicable`"""

    result_with_metadata = self._add_run_metadata(
        self.STATUS_NOT_APPLICABLE, message=message
    )

    self._results_to_tmpfile(result_with_metadata)

    sys.exit(0)


def exit_insufficient_data(self, message: str) -> None:
    """Exits the program early and puts status `insufficient_data`"""
    # Write output

    result_with_metadata = self._add_run_metadata(
        self.STATUS_INSUFFICIENT_DATA, message=message
    )

    self._results_to_tmpfile(result_with_metadata)

    sys.exit(0)


def notebook_not_found_s3(self) -> None:
    """Notebook could not be found/downloaded from S3. Not designed to be run from inside a notebook."""

    message = "Notebook could not be found/downloaded from S3. Check keys, file."

    result_with_metadata = self._add_run_metadata(
        self.STATUS_NOTEBOOK_NOT_FOUND_S3, message=message
    )

    self._results_to_tmpfile(result_with_metadata)

    pass
