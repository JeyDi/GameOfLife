import logging

from src.board import GameBoard


def game_status(GameBoard: GameBoard, tick: int):

    logging.debug(f"Updating game status: {tick}")
    alive = []
    killed = []

    for row in range(len(GameBoard._grid)):
        for column in range(len(GameBoard._grid[row])):

            neighbor = neighbor_settings(GameBoard, row, column)

            living = []

            for cell in neighbor:
                # check if a cell in the neighbor is alive:
                if cell.check_status():
                    living.append(cell)

            cell = GameBoard._grid[row][column]
            status_cell = cell.check_status()

            # Game of Life main rules
            if status_cell:
                if len(living) < 2 or len(living) > 3:
                    killed.append(cell)

                if len(living) == 3 or len(living) == 2:
                    alive.append(cell)

            else:
                if len(living) == 3:
                    alive.append(cell)

    # final update sett cell statuses
    for cell in alive:
        cell.set_alive()

    for cell in killed:
        cell.set_dead()

    logging.debug("Game status updated")


def neighbor_settings(
    GameBoard: GameBoard,
    current_row: int,
    current_col: int,
    neighbor_min=-1,
    neighbor_max=2,
) -> GameBoard:

    # logging.debug("Checking neighbors")

    # Build a square for research rules
    neighbor_list = []
    for row in range(neighbor_min, neighbor_max):
        for col in range(neighbor_min, neighbor_max):
            neighbor_row = current_row + row
            neighbor_col = current_col + col

            valid = True
            if neighbor_row == current_row and neighbor_col == current_col:
                valid = False
            if neighbor_row >= GameBoard._rows or neighbor_row < 0:
                valid = False
            if neighbor_col >= GameBoard._columns or neighbor_col < 0:
                valid = False
            if valid:
                neighbor_list.append(
                    GameBoard._grid[neighbor_row][neighbor_col]
                )

    # logging.debug(f"Neighbor checked: {neighbor_list}")
    return neighbor_list
