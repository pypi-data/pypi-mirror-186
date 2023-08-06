import os
import sys
from typing import Optional

from dotenv import load_dotenv
import typer

from lupin_grognard.__init__ import __version__
from lupin_grognard.core.check import check_commit, check_max_allowed_commits
from lupin_grognard.core.git import Git
from .core.tools.utils import (
    create_branch_list,
    display_current_branch_name,
    display_number_of_commits_to_check,
    generate_commit_list,
    generate_commits_range_to_check,
)

load_dotenv()
GROG_BRANCHES = os.getenv("GROG_BRANCHES")
GROG_MAX_ALLOWED_COMMITS = os.getenv("GROG_MAX_ALLOWED_COMMITS")


cli = typer.Typer()


@cli.command()
def version():
    print(f"Version: {__version__}")


@cli.command()
def check_commits(
    all: bool = typer.Option(
        False, "--all", "-a", help="check all commits from initial commit"
    ),
    grog_max_allowed_commits: int = typer.Option(
        1, "--grog-max-allowed-commits", "-max", envvar="GROG_MAX_ALLOWED_COMMITS"
    ),
    grog_dont_check_for_approvers: int = typer.Option(
        0,
        "--grog-dont-check-for-approvers",
        "-dont-approvers",
        envvar="GROG_DONT_CHECK_FOR_APPROVERS",
        min=0,
        max=1,
    ),
    branches_name: Optional[str] = typer.Argument(
        default="master, main, dev, development", envvar="GROG_BRANCHES"
    ),
):
    """
    Check every commit message since the last "merge request" in any of the branches in the branches_name list

    - With --all option :
    grog check-commits [--all or -a] to check all commits from initial commit

    - With --grog-max-allowed-commits option :
    grog check-commits [--grog-max-allowed-commits or -max] {int} to set the maximum number
    of commits allowed to the branch.
    Example : grog check-commits --grog-max-allowed-commits 10

    - With --grog-dont-check-for-approvers option :
    by default, grog check commits will check for approvers in the Merge commit.
    grog check-commits [--grog-dont-check-for-approvers or -dont-approvers] 1 to disable option

    - With branches_name argument: grog check-commits "branch_1, branch_2..."

    You can set GROG_BRANCHES, GROG_MAX_ALLOWED_COMMITS and GROG_DONT_CHECK_FOR_APPROVERS
    env var in .env, .gitlab-ci.yml, gitlab...
    """
    git = Git()
    if all:  # --all option
        git_log = git.get_log()
        grog_max_allowed_commits = 0
    else:
        git_log = git.get_log(max_line_count=50, first_parent=True)
    if git_log.stderr:
        print(f"git error {git_log.return_code}\n{git_log.stderr}")
        sys.exit(1)

    branch_list = create_branch_list(branches_name=branches_name)
    commit_list = generate_commit_list(data=git_log.stdout)
    display_current_branch_name()

    if all:  # --all option
        if check_max_allowed_commits(
            commits=commit_list, max_allowed_commits=grog_max_allowed_commits
        ):
            display_number_of_commits_to_check(commit_list=commit_list)
            check_commit(
                commits=commit_list, merge_option=grog_dont_check_for_approvers
            )
    else:
        commit_range_list_to_check = generate_commits_range_to_check(
            branch_list=branch_list, commit_list=commit_list
        )
        if check_max_allowed_commits(
            commits=commit_range_list_to_check,
            max_allowed_commits=grog_max_allowed_commits,
        ):
            display_number_of_commits_to_check(commit_list=commit_range_list_to_check)
            check_commit(
                commits=commit_range_list_to_check,
                merge_option=grog_dont_check_for_approvers,
            )
