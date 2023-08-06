"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Gridworks Protocol."""


if __name__ == "__main__":
    main(prog_name="gridworks-protocol")  # pragma: no cover
