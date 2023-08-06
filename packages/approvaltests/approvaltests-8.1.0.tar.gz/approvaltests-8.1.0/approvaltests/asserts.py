from typing import Optional

from approval_utilities.utils import write_to_temporary_file
from approvaltests.approvals import get_default_namer
from approvaltests.approvals import verify_with_namer
from approvaltests.namer.stack_frame_namer import StackFrameNamer
from approvaltests.reporters.default_reporter_factory import get_reporter
from approvaltests.reporters.testing_reporter import ReporterForTesting


class FilePathNamer(StackFrameNamer):
    def __init__(self, file_path: str, extension: None = None) -> None:
        StackFrameNamer.__init__(self, extension)
        self.file_path = file_path

    def get_approved_filename(self, basename: Optional[str] = None) -> str:
        return self.file_path


def assert_against_file(
    actual: str, file_path: str, reporter: Optional[ReporterForTesting] = None
) -> None:
    namer = FilePathNamer(file_path)
    verify_with_namer(actual, namer, reporter)


def assert_equal_with_reporter(expected, actual, reporter=None):
    if actual == expected:
        return

    name = get_default_namer().get_file_name()
    expected_file = write_to_temporary_file(expected, name + ".expected.")
    actual_file = write_to_temporary_file(actual, name + ".actual.")
    get_reporter(reporter).report(actual_file, expected_file)
    raise AssertionError(
        f'expected != actual\n  actual: "{actual}"\nexpected: "{expected}"'
    )
