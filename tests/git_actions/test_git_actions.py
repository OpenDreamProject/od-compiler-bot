from pathlib import Path
from time import sleep
from unittest.mock import patch

import git

from . import build_dir
from od_compiler.util.git_actions import updateOD
from od_compiler.util.git_actions import updateSubmodules


@patch("git.Repo")
@patch("git.Git")
def test_update_od():
    pass
