#!/usr/bin/env python

"""
Usage:
  ./main.py <directory>

Show info about files in a git repository and when they've changed

"""

import datetime
import os
import re
import sys
import docopt
import subprocess
import pprint

def get_commit_hashes(directory):
    if directory[-1] != '/':
        directory = "{}/".format(directory)
    pr = subprocess.Popen("/usr/bin/git log --date=raw",
                          cwd=os.path.dirname(directory),
                          shell=True, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
    (git_log, error) = pr.communicate()

    git_hashes = []
    log_lines = git_log.split('\n')
    last_commit = None
    for line in log_lines:
        if re.match('^commit', line):
            last_commit = line.split(" ", 1)[-1]
        if re.match("^Date: ", line):
            timestamp = line.split(":",1)[1].strip().split(" ", 1)[0]
            git_hashes.append((timestamp, last_commit))
            last_commit = None
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
    counter = 0
    commit_hashes = list(get_commit_hashes(directory))
    leng = len(commit_hashes)
    for timestamp, commit_hash in commit_hashes:
        timestamp = int(timestamp)
        commit_date = datetime.datetime.utcfromtimestamp(timestamp)
        if counter % 100:
            perc = int((counter / float(leng)) * 100)
            print perc,
            sys.stdout.flush()
        counter += 1
        for file_name in get_hash_info(commit_hash, directory):
            if file_name not in files:
                files[file_name] = (commit_date.strftime("%d-%m-%y %H:%M:%S"), commit_hash)
    print ""
    pprint.pprint(files, width=100)
    print "KABLAM"


def main():
    options = docopt.docopt(__doc__, version="foo")
    git_checkout = options["<directory>"]
    if not os.path.isdir(git_checkout):
        raise RuntimeError("<directory> must exist")
    get_files_and_change_commits(git_checkout)


if __name__ == "__main__":
    sys.exit(main())
