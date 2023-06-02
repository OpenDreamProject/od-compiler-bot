from pathlib import Path

import pytest


@pytest.fixture(scope="session", autouse=True)
def build_dir(tmp_path_factory) -> Path:
    """Build dir for each run"""
    build_dir = tmp_path_factory.mktemp("od_compile_test")
    return build_dir


@pytest.fixture(scope="session")
def od_repo_path(build_dir: Path) -> Path:
    od_repo = build_dir.joinpath("OpenDream")
    od_repo.mkdir()
    return od_repo
