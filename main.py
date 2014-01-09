#!/usr/bin/env python

"""
Usage:
  ./main.py <directory>

Show info about files in a git repository and when they've changed

"""

import os
import subprocess
import sys
import docopt


def get_commit_hashes(directory):
    pass


def get_hash_info(hash, directory):
    pass


def get_files_and_change_commits(directory):
    print directory
    pr = subprocess.Popen( "/usr/bin/git log",
                      cwd = os.path.dirname( './' ),
                      shell = True, stdout = subprocess.PIPE,
                      stderr = subprocess.PIPE)
    (out, error) = pr.communicate()

    print "Error : " + str(error)
    print "out : " + str(out)



def main():
    options = docopt.docopt(__doc__, version="foo")
    git_checkout = options["<directory>"]
    if not os.path.isdir(git_checkout):
        raise RuntimeError("<directory> must exist")
    get_files_and_change_commits(git_checkout)


if __name__ == "__main__":
  sys.exit(main())
