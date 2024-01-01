import time

import typer
from rich.progress import track


app = typer.Typer()


@app.command()
def progress():
    pass


if __name__ == "__main__":
    app()