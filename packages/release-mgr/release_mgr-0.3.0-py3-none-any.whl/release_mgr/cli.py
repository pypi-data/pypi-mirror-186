#!/usr/bin/env python3

import argparse
import os
import sys
from copy import deepcopy

from release_mgr.git import get_commit_for_tag, get_repo, git
from release_mgr.github import create_release
from release_mgr.release import release_notes_for_version
from release_mgr.version import Version
from release_mgr.version_files import update_version_files


def main():
    """
    A simple tool for managing software releases on GitHub.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--version",
        "-v",
        type=str,
        default="",
        help="Explicitly specify the new version to use.",
    )
    parser.add_argument(
        "--pre-release",
        "-l",
        help="Indicates this is a pre-release and the Github release will reflect this.",
        action="store_true",
    )
    parser.add_argument(
        "--draft",
        "-d",
        help="Indicates this is a draft release and the Github release will reflect this.",
        action="store_true",
    )
    parser.add_argument(
        "--skip-version-files",
        "-s",
        help="If provided, don't try to update version metadata files (package.json, setup.py etc.)",
        action="store_true",
    )
    parser.add_argument(
        "--skip-upload",
        help="If provided, don't try to create a release on github and don't push the commits / tags",
        action="store_true",
    )
    parser.add_argument(
        "--repo",
        "-r",
        type=str,
        default=None,
        help="The repository to create the release on in :owner/:repo format, "
        "will attempt to parse from git remotes if not given",
    )
    # TODO: Think about how this should work
    parser.add_argument(
        "--title",
        "-t",
        help="If given use the release name as the markdown title, "
        "otherwise title is omitted for Github style formatting.",
        action="store_true",
    )

    parser.add_argument(
        "--minor",
        "-m",
        help="Bump the minor version, ignored if --version is given.",
        action="store_true",
    )
    parser.add_argument(
        "--major",
        "-j",
        help="Bump the major version, ignored if --version is given.",
        action="store_true",
    )
    parser.add_argument(
        "--patch",
        "-p",
        help="Bump the patch version, ignored if --version is given.",
        action="store_true",
    )
    args = parser.parse_args()

    title = args.title
    version = args.version
    major, minor, patch = args.major, args.minor, args.patch

    if not any((patch, minor, major, version)):
        print("Must provide one of --version, --major, --minor, or --patch.")
        sys.exit(1)

    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("$GITHUB_TOKEN must be set.")
        sys.exit(1)

    last_version_commit, last_version = Version.latest_version()
    if version:
        version = Version.from_str(version)
    else:
        version = deepcopy(last_version)
        if patch:
            version.increment_patch()
        if minor:
            version.increment_minor()
        if major:
            version.increment_major()

    version_commit = get_commit_for_tag("HEAD")
    release_notes = release_notes_for_version(
        version,
        version_commit,
        last_version_commit,
    )

    if title:
        release_notes = f"# {version}\n\n{release_notes}"

    repo = args.repo or get_repo()

    print("Creating release", version, version_commit)
    print("Previous version", last_version, last_version_commit)
    print("Pre-release?", args.pre_release)
    print("Draft release?", args.draft)
    print("Repository", repo)
    print("============= Release Notes ============")
    print(release_notes)

    ans = input("Does this look correct? (y/N) ")
    if not ans.startswith("y"):
        return

    if not args.skip_version_files:
        update_version_files(version)

    git("tag", str(version))
    if not args.skip_upload:
        git("push", "--tags")

    try:
        if not args.skip_upload:
            create_release(
                token=token,
                repo=repo,
                tag_name=str(version),
                name=str(version),
                body=release_notes,
                draft=args.draft,
                prerelease=args.pre_release,
            )
    except Exception as exc:
        print("Failed to create release!")
        print(exc)


if __name__ == "__main__":
    main()
