import re
import sys
from typing import List

import emoji

from lupin_grognard.core.commit import Commit
from lupin_grognard.core.config import (
    PATTERN,
    FAILED,
    TITLE_FAILED,
    BODY_FAILED,
    SUCCESS,
    EMOJI_CHECK,
    EMOJI_CROSS,
    INITIAL_COMMIT,
)


def validate_commit_message(commit_msg: str, pattern: str) -> bool:
    if (
        commit_msg.startswith("Merge")
        or commit_msg.startswith("Revert")
        or commit_msg.startswith("fixup!")
        or commit_msg.startswith("squash!")
        or commit_msg in INITIAL_COMMIT
    ):
        return True
    return bool(re.match(pattern, commit_msg))


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


def check_commit(commits: List) -> List:
    title_checklist = []
    body_checklist = []
    for c in commits:
        commit = Commit(commit=c)
        check_commit = validate_commit_message(commit_msg=commit.title, pattern=PATTERN)
        title_checklist.append(check_commit)
        checked_commit_result = (
            f"validation_{check_commit} Commit {commit.hash[:6]}: {commit.title}"
        )
        checked_body_result = []
        if commit.body:
            for message in commit.body:
                check_body_message = validate_commit_message(
                    commit_msg=message, pattern=PATTERN
                )
                if check_body_message:  # must not start with a conventional message
                    body_checklist.append(False)
                    checked_body_result.append(message)
        display_commit_report(
            commit_message=checked_commit_result,
            body=checked_body_result,
        )
    if not display_check_result_report(
        title_checklist=title_checklist, body_checklist=body_checklist
    ):
        sys.exit(1)


def display_commit_report(commit_message: str, body: List = None):
    checked_message = commit_message.replace("validation_True", EMOJI_CHECK).replace(
        "validation_False", EMOJI_CROSS
    )
    print(emoji.emojize(checked_message))
    if len(body) > 0:
        print(emoji.emojize(f"{EMOJI_CROSS} Error in message discription:"))
        for message in body:
            print(f"    {message}")


def display_check_result_report(title_checklist: List, body_checklist: List) -> bool:
    error_number = title_checklist.count(False) + body_checklist.count(False)
    has_error_in_title = False in title_checklist
    has_error_in_body = False in body_checklist

    if has_error_in_title or has_error_in_body:
        print(FAILED)
        print(f"Errors found : {error_number}")
        if has_error_in_title and not has_error_in_body:
            print(TITLE_FAILED)
        elif has_error_in_body and not has_error_in_title:
            print(BODY_FAILED)
        else:
            print(f"{TITLE_FAILED}\n{BODY_FAILED}")
        return False
    else:
        print(SUCCESS)
        return True
