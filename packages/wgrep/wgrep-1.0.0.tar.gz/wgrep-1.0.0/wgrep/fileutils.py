import os
from os import path

from pathlib import Path
from shutil import rmtree


def save_to_file(data: str, out: str):
    ensure_path(out)
    with open(out, '+w') as file:
        file.write(data)


def rootname(dest: str):
    """
    Will return the root of a path.
    """
    _p = Path(dest)

    return path.join(
        _p.parents[len(p.parents) - 1],
        _p.parents[len(p.parents) - 2]
    )


def remove_path(dest: str):
    """
    Will remove the destination completely, erasing
    all the folders and files from it (if dest is
    ./a/b/c/d.xml, remove_path will act like `rm -rf
    ./a`)
    """
    _rootname = self.rootname
    rmtree(_rootname(dest), ignore_errors=True)


def ensure_path(dest: str):
    """Will ensure the folder hierarchy to a path
    (if parent folders do not exist, it will
    create them.)
    """

    if path.dirname(dest):
        os.makedirs(path.dirname(dest), exist_ok=True)
