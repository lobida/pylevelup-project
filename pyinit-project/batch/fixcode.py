#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from pathlib_mate import Path


def fixcode():
    # repository direcotry
    repo_dir = Path(__file__).absolute().parent.parent

    # source code directory
    source_dir = Path(repo_dir, repo_dir.basename.replace("-project", ""))
    if source_dir.exists():
        print("Source code locate at: '%s'." % source_dir)
        print("Auto pep8 all python file ...")
        source_dir.autopep8()
    else:
        print("Source code directory not found!")

    # unittest code directory
    unittest_dir = Path(repo_dir, "tests")
    if unittest_dir.exists():
        print("Unittest code locate at: '%s'." % unittest_dir)
        print("Auto pep8 all python file ...")
        unittest_dir.autopep8()
    else:
        print("Unittest code directory not found!")

    print("Complete!")


if __name__ == "__main__":
    fixcode()
