from typer.testing import CliRunner

from gpcrbeam.cli import app

runner = CliRunner()


def test_hello_default() -> None:
    result = runner.invoke(app, ["hello"], input=None)
    assert result.exit_code == 0
    assert "Hello, world!" in result.stdout
