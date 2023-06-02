from logging import CRITICAL

import pytest

from od_compiler import create_app


@pytest.fixture(scope="module")
def client():
    app = create_app(logger_override=CRITICAL)
    app.config.update(
        {
            "TESTING": True,
        }
    )

    with app.test_client() as client:
        yield client
