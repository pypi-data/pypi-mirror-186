import argparse
import sys

import requests
import toml


def main():
    parser = argparse.ArgumentParser(
        description="Verify version in pyproject.toml is not already used"
    )
    parser.add_argument(
        "repo_url",
        help="Full URL to github repo that tag should be checked",
        type=str,
    )
    parser.add_argument(
        "--pyproject_file",
        help="Path to pyproject.toml file",
        default="pyproject.toml",
        type=str,
    )
    args = parser.parse_args()

    with open(args.pyproject_file, "r") as f:
        pyproject_toml = toml.load(f)
        version = pyproject_toml["tool"]["poetry"]["version"]

    url = f"{args.repo_url}/releases/tag/{version}"
    r = requests.get(url=url, stream=True)
    # 404 means such a tag is not used, 200 otherwise
    if not r.status_code == 404:
        sys.exit(f"Tag {version} from {args.pyproject_file} already exists at {url}")
    print("OK")


if __name__ == "__main__":
    main()
