from argparse import ArgumentParser
from pathlib import Path
from subprocess import run, CalledProcessError
from sys import executable, exit
from shutil import rmtree, which
from os.path import relpath
from os import name as os_name
from wwpy.version import get_repo_version
from re import fullmatch


def get_package_dir() -> Path:
    return Path(__file__).parent


def get_project_dir() -> Path:
    return get_package_dir().parent


def get_requirements_path() -> Path:
    return get_project_dir() / "requirements.txt"


def get_version_path() -> Path:
    return get_package_dir() / "version.txt"


def get_dist_dir() -> Path:
    return get_project_dir() / "dist"


def get_envrc_path() -> Path:
    return get_project_dir() / ".envrc"


def get_venv_dir() -> Path:
    return get_project_dir() / ".venv"


def get_venv_executable() -> Path:
    if os_name == "nt":
        return get_venv_dir() / "Scripts/python.exe"
    else:
        return get_venv_dir() / "bin/python"


def get_tests_dir() -> Path:
    return get_package_dir() / "tests"


def get_git_hooks_dir() -> Path:
    return get_project_dir() / ".git/hooks"


def get_git_hooks_src_dir() -> Path:
    return get_package_dir() / "git_hooks"


def test():
    try:
        run(
            [executable, "-m", "flake8", get_package_dir(), "--max-line-length", "88"],
            check=True,
        )
    except CalledProcessError as err:
        exit(err.returncode)
    tests_dir = get_tests_dir()
    try:
        run([executable, "-m", "pytest", tests_dir], check=True, cwd=tests_dir)
    except CalledProcessError as err:
        exit(err.returncode)


def clean_distributions():
    rmtree(get_dist_dir())


def get_distributions() -> list[Path]:
    dist_dir = get_dist_dir()
    return [dist_dir / dist for dist in dist_dir.iterdir()]


def upload_distributions():
    distributions = get_distributions()

    assert len(distributions) == 2

    sdist = next(
        dist for dist in distributions
        if dist.name.endswith(".tar.gz")
    )
    whl = next(
        dist for dist in distributions
        if dist.name.endswith(".whl")
    )

    if (fullmatch(r"wwpy-[0-9]+\.[0-9]+.tar.gz", sdist.name)
            and fullmatch(r"wwpy-[0-9]+\.[0-9]+-py3-none-any.whl", whl.name)):
        run(
            [
                executable,
                "-m",
                "twine",
                "upload",
                "--non-interactive",
                "-u", "__token__",
                *distributions,
            ],
            check=True,
        )
    elif (fullmatch(
            r"wwpy-[0-9]+\.[0-9]+\.dev[0-9]+\+[0-9A-Za-z\.]+.tar.gz",
            sdist.name
        )
        and fullmatch(
            r"wwpy-[0-9]+\.[0-9]+\.dev[0-9]\+[0-9A-Za-z\.]+-py3-none-any.whl",
            whl.name)):
        # Development distribution. Don't need to upload.
        pass
    else:
        raise AssertionError(f"Invalid dist names: {sdist.name}, {whl.name}")


def deploy():
    build()
    upload_distributions()


def freeze_requirements():
    requirements = run(
        [executable, "-m", "pip", "freeze", "--all", "--exclude-editable"],
        text=True,
        check=True,
        capture_output=True,
    ).stdout
    with open(get_requirements_path(), "w") as requirements_file:
        requirements_file.write(requirements)


def setup_venv():

    resolved_executable = Path(executable).resolve()
    venv_dir = get_venv_dir()
    try:
        rmtree(venv_dir)
    except FileNotFoundError:
        pass
    run([resolved_executable, "-m", "venv", venv_dir], check=True)


def install_packages():
    # The requirements.txt packages are installed before wppy to pin the
    # package versions
    run(
        [
            get_venv_executable(),
            "-m",
            "pip",
            "install",
            "-r",
            get_requirements_path(),
        ],
        check=True,
    )
    run(
        [get_venv_executable(), "-m", "pip", "install", "-e", get_project_dir()],
        check=True,
    )


def setup_direnv():
    if os_name == "nt":
        # direnv doesn't run on Windows. Also note that the envrc references
        # the activation script for the Unix install. On Windows, it is under
        # .venv/Scripts.
        return
    if not which("direnv"):  # Don't setup if direnv is not installed
        return
    envrc_path = get_envrc_path()
    with open(envrc_path, "w") as envrc_file:
        envrc_file.write(
            """source .venv/bin/activate

# PS1 cannot be exported. For more information see
# https://github.com/direnv/direnv/wiki/PS1
unset PS1
"""
        )
    run(["direnv", "allow", envrc_path], check=True)


git_hook_names = ["pre-commit", "post-checkout"]


def setup_git_hooks():
    git_hooks_dir = get_git_hooks_dir()
    relative_src_dir = Path(relpath(get_git_hooks_src_dir(), git_hooks_dir))

    for hook_name in git_hook_names:
        hook_path = git_hooks_dir / hook_name
        hook_path.unlink(missing_ok=True)
        hook_path.symlink_to(relative_src_dir / (hook_name.replace("-", "_") + ".py"))


def setup():
    setup_venv()
    install_packages()
    setup_direnv()
    setup_git_hooks()


def build():
    version_path = get_version_path()
    with open(version_path, "w") as version_file:
        version_file.write(get_repo_version(get_project_dir()))
    run(
        [executable, "-m", "build", get_project_dir()],
        check=True,
    )


def main():
    parser = ArgumentParser()
    main_subparsers = parser.add_subparsers(dest="main", required=True)

    main_subparsers.add_parser("test")
    main_subparsers.add_parser("deploy")
    main_subparsers.add_parser("freeze-requirements")
    main_subparsers.add_parser("setup")
    main_subparsers.add_parser("build")

    args = parser.parse_args()

    function = globals()[args.main.replace("-", "_")]

    function()


if __name__ == "__main__":
    main()
