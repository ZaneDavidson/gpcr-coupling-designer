import typer

from gpcrbeam import __version__

app = typer.Typer(
    help=(
        "GPCRBeam: An inference pipeline for determining the native "
        "G-protein coupling of a GPCR protein based on sequence analysis."
    ),
    no_args_is_help=True,
    add_completion=True,
)


@app.callback(invoke_without_command=True)
def main(
    version: bool = typer.Option(
        False,
        "--version",
        "-v",
        help="Show version and exit.",
        is_eager=True,
    ),
) -> None:
    if version:
        typer.echo(__version__)
        raise typer.Exit()


@app.command(help="Say hello.")
def hello(name: str | None = "world") -> None:
    typer.echo(f"Hello, {name}!")


if __name__ == "__main__":
    app()
