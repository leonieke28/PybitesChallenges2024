import pytest
from typer.testing import CliRunner

from script import app


@pytest.fixture()
def runner() -> CliRunner:
    return CliRunner()