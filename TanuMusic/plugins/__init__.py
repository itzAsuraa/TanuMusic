import glob
import logging
import os
import shutil
import sys
from os.path import abspath, dirname, isfile, join

from TanuMusic import LOGGER

logger = LOGGER(__name__)

if "utils" in os.listdir():
    shutil.rmtree("utils")

ROOT_DIR = abspath(join(dirname(__file__), "..", ".."))

def __list_all_modules():
    main_repo_plugins_dir = dirname(__file__)
    work_dirs = [main_repo_plugins_dir]

    all_modules = []

    for work_dir in work_dirs:
        mod_paths = glob.glob(join(work_dir, "*.py"))
        mod_paths += glob.glob(join(work_dir, "*/*.py"))

        modules = [
            (f.replace(main_repo_plugins_dir, "TanuMusic.plugins")).replace(os.sep, ".")[:-3]
            for f in mod_paths
            if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
        ]
        all_modules.extend(modules)

    return all_modules


ALL_MODULES = sorted(__list_all_modules())
__all__ = ALL_MODULES + ["ALL_MODULES"]