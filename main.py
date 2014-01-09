#!/usr/bin/env python

"""
Usage:
  ./main.py <directory>

Show info about files in a git repository and when they've changed

"""

import os
import re
import sys
import docopt
import subprocess


def get_commit_hashes(directory):
    if directory[-1] != '/':
        directory = "{}/".format(directory)
    pr = subprocess.Popen("/usr/bin/git log",
                          cwd=os.path.dirname(directory),
                          shell=True, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
    (git_log, error) = pr.communicate()

    git_hashes = []
    log_lines = git_log.split('\n')
    for line in log_lines:
        if re.match('^commit', line):
            git_hashes.append(line[7:])

    return reversed(git_hashes)


def get_hash_info(commit_hash, directory):
    """
    Get information for commit hash.

    hash - Commit
    directory - git repo dir

    """
    cmd = "cd %s && git ls-tree --name-only -r %s" % (directory, commit_hash)
    info = subprocess.check_output(cmd, shell=True)
    info = info.split("\n")
    info = [line for line in info if line != ""]
    return info


def get_files_and_change_commits(directory):
    files = {}
    for commit_hash in get_commit_hashes(directory):
        print ".",
        sys.stdout.flush()
        for file_name in get_hash_info(commit_hash, directory):
            print ".",
            sys.stdout.flush()
            if file_name not in files:
                files[file_name] = commit_hash
    print ""
    print files


def main():
    options = docopt.docopt(__doc__, version="foo")
    git_checkout = options["<directory>"]
    if not os.path.isdir(git_checkout):
        raise RuntimeError("<directory> must exist")
    get_files_and_change_commits(git_checkout)


if __name__ == "__main__":
    sys.exit(main())
