import sys
from typing import List

from lupin_grognard.core.commit.commit_validator import CommitValidator
from lupin_grognard.core.commit.commit_error import ErrorCount


def check_max_allowed_commits(commits: List, max_allowed_commits: int):
    if max_allowed_commits == 0:
        return True
    elif len(commits) > max_allowed_commits:
        print(
            f"Error: found {len(commits)} commits to check in the"
            f"current branch while the maximum allowed number is {max_allowed_commits}"
        )
        sys.exit(1)
    return True


def check_commit(commits: List, merge_option: int) -> None:
    """
    check_commit performs validation checks on each commit.
    If merge_option is set to 0, the function checks that merge commits
    have approvers and validates the commits title and body.
    If merge_option is 1, the function only validates the commit title and body.
    The function also calls the error_report method of the ErrorCount
    class to output any errors found during validation.
    If any errors are found, it will call sys.exit(1)
    Args:
        commits (List): List of commits to check
        merge_option (int): 0 or 1
    """
    for c in commits:
        commit = CommitValidator(commit=c)
        if merge_option == 0:  # check merge commits have approvers
            if commit.title.startswith("Merge"):
                if not commit.validate_commit_merge():
                    commit.error_count.increment_merge_error()
            elif not commit.validate_commit_title():
                commit.error_count.increment_title_error()
            if not commit.validate_commit_body():
                commit.error_count.increment_body_error()
        elif merge_option == 1:
            if not commit.validate_commit_title():
                commit.error_count.increment_title_error()
            if not commit.validate_commit_body():
                commit.error_count.increment_body_error()
    ErrorCount.error_report()
