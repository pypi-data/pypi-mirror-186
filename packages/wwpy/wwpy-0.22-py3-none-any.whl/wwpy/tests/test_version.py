from wwpy.version import get_repo_version
from pytest import fixture
from subprocess import run
from pathlib import Path


@fixture
def repo(tmp_path):
    run(
        ["git", "init", "--bare", "testproject.git"],
        cwd=tmp_path,
        check=True
    )
    run(
        ["git", "clone", tmp_path / "testproject.git"],
        cwd=tmp_path,
        check=True
    )
    repo_path = tmp_path / "testproject"
    run(
        ["git", "checkout", "-b", "main"],
        cwd=repo_path,
        check=True,
    )
    commit(repo_path)
    push(repo_path)
    yield repo_path


def push(repo: Path):
    run(["git", "push", "origin", "HEAD"], cwd=repo, check=True)


def commit(repo: Path):
    file_path = repo / "foo.txt"
    with open(file_path, "a") as file_:
        file_.write("bump\n")
    run(["git", "add", file_path], cwd=repo, check=True)
    run(["git", "commit", "-m", "bump"], cwd=repo, check=True)


def checkout_new_branch(repo: Path, branch_name: str):
    run(["git", "checkout", "-b", branch_name], cwd=repo, check=True)


def checkout(repo: Path, branch_name: str):
    run(["git", "checkout", branch_name], cwd=repo, check=True)


def merge(repo: Path, branch_name: str):
    run(["git", "merge", "--no-ff", branch_name], cwd=repo, check=True)


def test_version_in_new_repository(repo: Path):
    assert get_repo_version(repo) == "0.1"


def test_version_after_single_commit(repo: Path):
    commit(repo)
    push(repo)
    assert get_repo_version(repo) == "0.2"


def test_version_after_multi_commit_merge(repo: Path):
    checkout_new_branch(repo, "new-branch")
    commit(repo)
    commit(repo)
    checkout(repo, "main")
    merge(repo, "new-branch")
    push(repo)
    assert get_repo_version(repo) == "0.2"


def test_version_after_commit_and_merge(repo: Path):
    checkout_new_branch(repo, "new-branch")
    commit(repo)
    checkout(repo, "main")
    merge(repo, "new-branch")
    commit(repo)
    push(repo)
    assert get_repo_version(repo) == "0.3"


def test_version_on_feature_branch(repo: Path):
    checkout_new_branch(repo, "new-branch")
    assert get_repo_version(repo) == "0.2.dev0+newbranch"


def test_version_on_feature_branch_after_commit(repo: Path):
    checkout_new_branch(repo, "new-branch")
    commit(repo)
    assert get_repo_version(repo) == "0.2.dev1+newbranch"


def test_version_on_feature_branch_after_multiple_commits(repo: Path):
    checkout_new_branch(repo, "new-branch")
    commit(repo)
    commit(repo)
    assert get_repo_version(repo) == "0.2.dev2+newbranch"
