import sys

from lupin_grognard.core.config import (
    SUCCESS,
    FAILED,
    TITLE_FAILED,
    BODY_FAILED,
    MERGE_FAILED,
)


class ErrorCount:
    title_error = 0
    body_error = 0
    merge_error = 0

    def __init__(self):
        pass

    @classmethod
    def increment_title_error(cls):
        cls.title_error += 1

    @classmethod
    def increment_body_error(cls):
        cls.body_error += 1

    @classmethod
    def increment_merge_error(cls):
        cls.merge_error += 1

    @classmethod
    def error_report(cls):
        if cls.title_error == 0 and cls.body_error == 0 and cls.merge_error == 0:
            print(SUCCESS)
        else:
            print(FAILED)
            print(f"Errors found: {cls.title_error + cls.body_error + cls.merge_error}")
            if cls.title_error > 0:
                print(TITLE_FAILED)
            if cls.body_error > 0:
                print(BODY_FAILED)
            if cls.merge_error > 0:
                print(MERGE_FAILED)
            sys.exit(1)
