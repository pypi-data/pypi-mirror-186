from typing import List


class Commit:
    def __init__(self, commit: str):
        self.commit = commit

    @property
    def hash(self) -> str:
        start = "hash>>"
        end = "<<hash"
        start_index = self.commit.find(start) + len(start)
        end_index = self.commit.find(end)
        return self.commit[start_index:end_index]

    @property
    def title(self) -> str:
        start = "title>>"
        end = "<<title"
        index_start = self.commit.find(start) + len(start)
        index_end = self.commit.find(end)
        return self.commit[index_start:index_end]

    @property
    def body(self) -> List:
        start = "body>>"
        end = "<<body"
        index_start = self.commit.find(start) + len(start)
        index_end = self.commit.find(end)
        body = self.commit[index_start:index_end]
        return [message for message in body.split("\n") if len(message) > 0]
