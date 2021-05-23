import logging
from random import randint


from src.status import Cell


class GameBoard:
    def __init__(self, rows: int, columns: int, max_prob=2):
        self._rows = rows
        self._columns = columns

        # Define the grid
        self._grid = [
            [Cell() for c in range(self._columns)] for r in range(self._rows)
        ]

        logging.debug(
            f"Board generated with: {rows} rows, and {columns} columns"
        )

        # Build the board
        self._build_board(max_prob)

        logging.info("Initial board generated")

    def _build_board(self, max_prob: int):
        logging.debug("Building the board")
        for r in self._grid:
            for c in r:
                # set the probability to spawn a living cell
                probability = randint(0, max_prob)                
                if probability == 1:
                    c.set_alive()

    def print_board(self, tick: int):
        logging.info("\n\n\n\n")
        logging.info(f"Board status tick: {tick}")
        for r in self._grid:
            for c in r:
                print(f"{c.print_status()}", end="")
            print()
