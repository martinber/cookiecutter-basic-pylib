#!/usr/bin/env python
import os
import subprocess


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def git_init():
    subprocess.call(["git", "init"])


if __name__ == "__main__":

    git_init()
