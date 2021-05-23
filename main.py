"""
    Game of Life: Object plain python implementation
    Author: Andrea Guzzo (JeyDi)
"""
import time
import typer
import logging


from config import configure_logging, ROWS, COLUMNS, MAX_PROB

from src.board import GameBoard
from src.rules import game_status


def main(
    user: int = typer.Option(1, min=0, max=1),
    rows: int = typer.Option(40, min=10),
    columns: int = typer.Option(40, min=10),
    max_prob: int = typer.Option(2, min=2, max=9),
    max_tick: int = typer.Option(60, min=-1),
    sleep: int = typer.Option(1, min=1),
    verbosity: str = typer.Option("info"),
):

    # Configure the logging
    configure_logging(verbosity, "./logs")

    # Use typer
    if user == "1":
        # Ask for the user value input
        rows = int(typer.prompt("Insert the number of rows"))
        columns = int(typer.prompt("Insert the number of columns"))
        max_prob = int(
            typer.prompt(
                "Insert the probability of spawning a new living cell"
            )
        )
        max_tick = int(
            typer.prompt(
                "Insert the number of iterations you want to observe (-1 for endless)"
            )
        )
        launch = typer.confirm("Do you want to launch the simulation?")
        if not launch:
            message = typer.style("Ok! Bye...", fg=typer.colors.RED, bold=True)
            typer.echo(message)
            raise typer.Abort()
        message = typer.style("Launching...", fg=typer.colors.GREEN, bold=True)
        typer.echo(message)

    # Define the simulation default parameters
    if rows == 0:
        rows = ROWS
    if columns == 0:
        columns = COLUMNS
    if max_prob == 0:
        max_prob = MAX_PROB

    tick = 0
    logging.info("Launching the game")

    logging.debug(f"Rows: {rows}")
    logging.debug(f"Columns: {columns}")
    logging.debug(f"Max_prob: {max_prob}")
    logging.debug(f"Max Ticks: {max_tick}")
    logging.debug(f"Verbosity: {verbosity}")
    logging.debug(f"Max Ticks: {sleep}")
    logging.debug(f"Alive probability: {1/(max_prob+1)}")

    # create a board:
    game_board = GameBoard(rows, columns, max_prob)

    # run the first iteration of the board:
    game_board.print_board(tick)

    # Update the game status for every tick
    while tick <= max_tick:
        logging.debug(f"Tick: {tick}")
        game_status(game_board, tick)
        time.sleep(sleep)
        tick += 1
        game_board.print_board(tick)


if __name__ == "__main__":
    typer.run(main)
