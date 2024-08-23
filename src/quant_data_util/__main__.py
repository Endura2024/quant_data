"""Command-line interface."""

import click


@click.command()
@click.version_option()
def main() -> None:
    """Quant_Data."""


if __name__ == "__main__":
    main(prog_name="quant_data")  # pragma: no cover
