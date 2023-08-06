from datetime import datetime
from typing import List, Optional


class Commit:
    def __init__(self, commit: str):
        self.commit = commit

    @property
    def hash(self) -> str:
        return self._extract(start="hash>>")

    @property
    def author(self) -> str:
        return self._extract(start="author>>")

    @property
    def author_mail(self) -> str:
        return self._extract(start="author_mail>>")

    @property
    def author_date(self) -> str:
        timestamp = self._extract(start="author_date>>")
        date_object = datetime.fromtimestamp(int(timestamp))
        return date_object.strftime("%A %d %B %Y %H:%M:%S")

    @property
    def title(self) -> str:
        return self._extract(start="title>>")

    @property
    def body(self) -> Optional[List]:
        body = self._extract(start="body>>", end="<<body")
        if body == "":
            return None
        return [message for message in body.split("\n") if len(message) > 0]

    @property
    def closes_issues(self) -> str:
        if self.body:
            for line in self.body:
                if line.startswith("Closes #"):
                    return line.split("Closes #")[1]
        return "Not found"

    @property
    def approvers(self) -> List:
        approvers = []
        if self.body:
            for line in self.body:
                if line.startswith("Approved-by: "):
                    approvers.append(line.split("Approved-by: ")[1])
            return approvers
        return list()

    def _extract(self, start: str, end: str = "\n") -> str:
        start_index = self.commit.find(start) + len(start)
        return self.commit[start_index:self.commit.find(end, start_index)]
