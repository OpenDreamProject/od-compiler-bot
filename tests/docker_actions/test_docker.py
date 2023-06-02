import shutil
from os import chdir

import pytest

from od_compiler.util.docker_actions import compileOD


@pytest.mark.order("last")
def test_image_bulder(build_dir):
    shutil.copytree("docker", f"{build_dir}/docker")
    code = 'world.log << "Hello, pytest!"'

    chdir(build_dir)
    test_output = compileOD(codeText=code, compile_args=[""], timeout=30)
    assert test_output.keys() >= {"compiler", "server", "timeout"}
