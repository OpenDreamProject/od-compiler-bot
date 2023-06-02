import shutil
from pathlib import Path

import pytest
from git.repo import Repo

from tests import build_dir


@pytest.fixture(name="repo")
def repo_(tmp_path: Path) -> Repo:
    repo_path = tmp_path / "test_data"
    shutil.copytree("tests/git_actions/test_data", repo_path)

    return Repo.init(repo_path)
