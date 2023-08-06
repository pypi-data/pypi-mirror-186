import re

from lupin_grognard.core.commit.commit import Commit
from lupin_grognard.core.commit.commit_reporter import CommitReporter
from lupin_grognard.core.commit.commit_error import ErrorCount
from lupin_grognard.core.config import (
    INITIAL_COMMIT,
    EMOJI_CHECK,
    EMOJI_CROSS,
    PATTERN,
)


class CommitValidator(Commit):
    def __init__(self, commit: str):
        super().__init__(commit=commit)
        self.reporter = CommitReporter(commit)
        self.error_count = ErrorCount

    def validate_commit_title(self) -> bool:
        if self._validate_commit_message(self.title):
            self.reporter.display_title_report(EMOJI_CHECK)
            return True
        self.reporter.display_title_report(EMOJI_CROSS)
        return False

    def validate_commit_body(self) -> bool:
        if self.body:
            message_error = []
            for message in self.body:
                if self._validate_commit_message(message):
                    message_error.append(message)
            if len(message_error) > 0:
                self.reporter.display_body_report(message_error)
                return False  # must not start with a conventional message
        return True

    def validate_commit_merge(self) -> bool:
        self.reporter.display_merge_report(approvers=self.approvers)
        if len(self.approvers) < 1:
            return False
        return True

    def _validate_commit_message(self, commit_msg: str, pattern: str = PATTERN) -> bool:
        if (
            commit_msg.startswith("Merge")
            or commit_msg.startswith("Revert")
            or commit_msg.startswith("fixup!")
            or commit_msg.startswith("squash!")
            or commit_msg in INITIAL_COMMIT
        ):
            return True
        return bool(re.match(pattern, commit_msg))
