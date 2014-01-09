#!/usr/bin/env python

"""
Usage:
  ./main.py <directory>

Show info about files in a git repository and when they've changed
"""

import subprocess
import sys
import docopt


def get_commit_hashes(directory):
    pass


def get_hash_info(hash, directory):
    pass


def get_files_and_change_commits(directory):
    pass


def main():
    options = docopt.docopt(__doc__, version="foo")
    get_files_and_change_commits(options["directory"])


if __name__ == "__main__":
  sys.exit(main())
