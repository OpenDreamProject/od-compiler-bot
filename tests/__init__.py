from pathlib import Path

import pytest


@pytest.fixture(scope="session", autouse=True)
def build_dir(tmp_path_factory) -> Path:
    build_dir = tmp_path_factory.mktemp("od_compile_test")
    return build_dir
