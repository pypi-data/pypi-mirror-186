from pathlib import Path
from subprocess import run
from re import sub


def _get_main_rev_count(repo_path) -> str:
    return int(
        run(
            [
                "git",
                "rev-list",
                "--first-parent",
                "--count",
                "origin/main",
            ],
            check=True,
            text=True,
            cwd=repo_path,
            capture_output=True
        ).stdout
    )


def get_repo_version(repo_path: Path) -> str:
    current_branch = run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        check=True,
        text=True,
        cwd=repo_path,
        capture_output=True,
    ).stdout.rstrip()

    main_rev_count = _get_main_rev_count(repo_path)

    if current_branch == "main":
        return f"0.{main_rev_count}"
    else:
        branch_revision = int(
            run(
                ["git", "rev-list", "--count", "HEAD", "^origin/main"],
                check=True,
                text=True,
                cwd=repo_path,
                capture_output=True,
            ).stdout
        )

        cleaned_current_branch = sub(r"[^0-9a-zA-Z]", "", current_branch)

        prerelease = f"0.{main_rev_count + 1}"
        return f"{prerelease}.dev{branch_revision}+{cleaned_current_branch}"
