#!/usr/bin/env python3
import json
import argparse
import os.path
import git
import re
from packaging import version
import sys
import pathlib

script_path = pathlib.Path(__file__).parent.absolute()

__version__ = "0.0.4"


def get_git_root(path: str) -> str:
    git_repo = git.Repo(path, search_parent_directories=True)
    git_root = git_repo.git.rev_parse("--show-toplevel")
    return git_root


def args_parser_init() -> argparse.Namespace:
    """Get user inputs"""
    parser = argparse.ArgumentParser(
        description="""A tool for tagging wdl
Get more info at:
    https://workflows-dev-documentation.readthedocs.io/en/latest/Developer%20tools.html#wdl-tagging""",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "-w",
        "--input-wdl",
        type=str,
        required=True,
        help="The path to tagged .wdl file. In the same directory should be meta.json",
    )
    parser.add_argument(
        "-r",
        "--input-repository",
        type=str,
        required=False,
        default=get_git_root(script_path),
        help="A path to catalog containing .git file",
    )
    parser.add_argument(
        "-i",
        "--ignore-meta",
        required=False,
        default=False,
        action="store_true",
        help="Don't compare versions between meta.json and .wdl file",
    )
    parser.add_argument(
        "-v", "--version", action="version", version="%(prog)s {}".format(__version__)
    )

    args = parser.parse_args()
    return args


def get_version_from_wdl(wdl_path: str) -> str:
    mandatory = ["version", "String"]
    possible = ["pipeline", "module", "task"]
    workflow_version = get_from_wdl_line(wdl_path, mandatory, possible)

    return workflow_version


def get_workflow_from_wdl(wdl_path: str) -> str:
    mandatory = ["name", "String"]
    possible = ["pipeline", "module", "task"]
    raw_workflow_name = get_from_wdl_line(wdl_path, mandatory, possible)
    workflow_name = raw_workflow_name.replace("_", "-")

    return workflow_name


def get_from_wdl_line(wdl_path: str, mandatory: list, possible: list) -> str:
    with open(wdl_path) as wdl_file:
        containing_line = next(
            line
            for line in wdl_file
            if all(element in line for element in mandatory)
            and any(element in line for element in possible)
        )

        containing = re.findall('"([^"]*)"', containing_line)[0]
        return containing


def get_meta_json(meta_path: str) -> dict:
    with open(meta_path) as meta_file:
        meta_json = json.load(meta_file)
        return meta_json


def get_latest_semantic_version(checked_versions: list) -> str:
    latest_version = list(checked_versions)[0]

    for checked_version in checked_versions:
        if version.parse(checked_version) > version.parse(latest_version):
            latest_version = checked_version

    return latest_version


def get_latest_meta_version(meta_json: dict) -> str:
    versions_dict = meta_json["changes"]
    raw_versions = list(versions_dict.keys())
    latest_version = get_latest_semantic_version(raw_versions)

    return latest_version


def confirm() -> bool:
    answer = ""
    while answer not in ["y", "n"]:
        answer = input("Are you aware of this and want to continue [Y/N]? ").lower()
    return answer == "y"


def check_if_continue_program():
    if not confirm():
        sys.exit("You chose to quit the tagging process")


def compare_wdl_meta_versions(wdl_version: str, meta_version: str):
    if version.parse(wdl_version) != version.parse(meta_version):
        print(
            f"WDL version [{wdl_version}] is not compatible with latest version in meta changes [{meta_version}].\n"
            f"Check both wdl file and meta.json before commiting."
        )
        check_if_continue_program()


def get_and_sort_tags(git_repository: git.Repo) -> list:
    referenced_ = git_repository.tags
    return sorted(referenced_, key=lambda t: t.commit.committed_datetime)


def get_git_repository(repository_path: str):
    return git.Repo(repository_path)


def check_if_new_tag_in_tags(
    new_tag: str, clean_tags: list, last_tag_commit_author: str
):
    if new_tag in clean_tags:
        raise ValueError(
            f"Tag [{new_tag}] is currently occupied.\n"
            f"Check if someone forgot to merge changes.\n"
            f"This person may be {last_tag_commit_author}."
        )


def fetch_all_remotes(git_repository: git.Repo):
    for remote in git_repository.remotes:
        remote.fetch()
        print(f"Fetched: {remote}")


def check_if_new_tag_is_the_newest(
    new_tag: str, latest_version: str, last_tag_commit_author: str
):
    if version.parse(new_tag) < version.parse(latest_version):
        print(
            f"Your tag [{new_tag}] is older than latest tag [{latest_version}].\n"
            f"Currently, someone may be working with the same wdl and tagged it with higher version.\n"
            f"This person may be {last_tag_commit_author}.\n"
            f"If you are not fixing bugs in previous version, then you need to ask the person who is "
            f"making changes to merge them to dev.\n"
            f"Then merge dev to your branch and try to tag wdl again."
        )
        check_if_continue_program()


def get_file_content(input_file: str) -> str:
    with open(input_file, "r") as opened_file:
        return opened_file.read()


def get_last_commit_author(
    git_repository: git.Repo, tag_or_branch: str, input_wdl: str
) -> str:
    return git_repository.git.log(
        f"refs/tags/{tag_or_branch}", pretty="format:'%an'"
    ).split("\n")[0]


def check_if_dev_compatible_with_latest(
    git_repository: git.Repo,
    latest_tag: str,
    input_wdl: str,
    last_tag_commit_author: str,
):
    dev_branch = "dev"

    # in future could be simplified to git diff one file between tag and dev

    files_diff = git_repository.git.diff(
        f"refs/tags/{latest_tag}..origin/{dev_branch}", name_only=True
    )
    files_diff_list = files_diff.split("\n")
    if input_wdl in files_diff_list:
        print(
            "Latest tagged wdl version is not compatible with wdl on dev branch.\n"
            "Currently, someone may be working with the same wdl and tagged it with higher version.\n"
            f"This person may be {last_tag_commit_author}."
        )
        check_if_continue_program()


def create_and_push_new_tag(
    new_tag: str,
    referenced_tags: list,
    workflow_name: str,
    git_repository: git.Repo,
    input_wdl: str,
):
    clean_tags = [
        str(tag) for tag in referenced_tags if workflow_name == str(tag).split("@")[0]
    ]
    if not clean_tags:
        print(
            f"No active tags detected for {workflow_name} workflow. Probably this is the first version tagged.\n"
            "Continuing will skip checking the compatibility with the last version, which was not found."
        )
        check_if_continue_program()

    if clean_tags:
        name = clean_tags[0].split("@")[0]

        versions = [ver.split("@")[1] for ver in clean_tags]
        latest_version = get_latest_semantic_version(versions)
        latest_tag = f"{name}@{latest_version}"

        new_version = new_tag.split("@")[1]
        last_tag_commit_author = get_last_commit_author(
            git_repository, latest_tag, input_wdl
        )

        check_if_new_tag_in_tags(new_tag, clean_tags, last_tag_commit_author)
        check_if_new_tag_is_the_newest(
            new_version, latest_version, last_tag_commit_author
        )
        check_if_dev_compatible_with_latest(
            git_repository, latest_tag, input_wdl, last_tag_commit_author
        )

    tag_to_push = git_repository.create_tag(
        new_tag, message='Automatic tag "{0}"'.format(new_tag)
    )
    print(f"Tag [{new_tag}] has been created")
    git_repository.remotes.origin.push(tag_to_push)
    print(f"Tag [{new_tag}] has been pushed to remote")


def prepare_and_push_tag(
    git_repository: git.Repo, workflow_name: str, input_tag: str, input_wdl: str
):
    referenced_tags = get_and_sort_tags(git_repository)
    new_tag = f"{workflow_name}@{input_tag}"
    create_and_push_new_tag(
        new_tag, referenced_tags, workflow_name, git_repository, input_wdl
    )


def set_and_compare_wdl_meta_versions(input_wdl: str, input_meta_json: str):
    wdl_version = get_version_from_wdl(input_wdl)
    meta_json = get_meta_json(input_meta_json)
    meta_version = get_latest_meta_version(meta_json)
    compare_wdl_meta_versions(wdl_version, meta_version)


def get_meta_json_path(input_wdl: str):
    wdl_dir = os.path.dirname(input_wdl)
    return f"{wdl_dir}/meta.json"


def get_wdl_path(input_wdl_dir: str) -> str:
    catalog_name = os.path.basename(input_wdl_dir)
    wdl_name = f"{catalog_name}.wdl"
    return f"{input_wdl_dir}/{wdl_name}"


def check_if_paths_exist(paths=list):
    for path in paths:
        if not os.path.exists(path):
            raise FileExistsError(
                f"[{path}] file path does not exist.\n"
                f"Check naming meta.json and .wdl file rules in docs: "
                f"https://workflows-dev-documentation.readthedocs.io/en/latest/Developer%20tools.html#wdl-tagging"
            )


def main():
    args = args_parser_init()

    if not args.ignore_meta:
        meta_json_path = get_meta_json_path(args.input_wdl)
        paths = [meta_json_path, args.input_wdl]
        set_and_compare_wdl_meta_versions(args.input_wdl, meta_json_path)
    else:
        paths = [args.input_wdl]

    check_if_paths_exist(paths)
    
    git_repository = get_git_repository(args.input_repository)
    print(f"Git repository: [{git_repository}]")
    fetch_all_remotes(git_repository)

    wdl_version = get_version_from_wdl(args.input_wdl)
    workflow_name = get_workflow_from_wdl(args.input_wdl)
    prepare_and_push_tag(git_repository, workflow_name, wdl_version, args.input_wdl)


if __name__ == "__main__":
    main()
