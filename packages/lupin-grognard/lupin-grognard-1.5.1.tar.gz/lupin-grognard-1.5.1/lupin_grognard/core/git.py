from lupin_grognard.core.cmd import Command, run_command
from lupin_grognard.core.config import COMMIT_DELIMITER


class Git:
    def get_log(
        self, max_line_count: int = None, first_parent: bool = False
    ) -> Command:
        # format = "hash>>%H<<hash%ntitle>>%s<<title%nbody>>%b<<body%n"
        format: str = "hash>>%H%nauthor>>%cN%nauthor_mail>>%cE%nauthor_date>>%ct%ntitle>>%s%nbody>>%b<<body%n"
        delimiter = COMMIT_DELIMITER
        if first_parent:
            command = f'git log --first-parent --format="{format}"{delimiter}'
        else:
            command = f'git log --format="{format}"{delimiter}'
        if max_line_count:
            max_count = f"--max-count={max_line_count}"
            command = f"{command} {max_count}"
        return run_command(command=command)

    def get_branch_name(self) -> str:
        return run_command(command="git branch --show-current").stdout
