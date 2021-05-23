# GameOfLife

Simple implementation of Conway's Game of Life.

The implementation is written in full vanilla python and it's object oriented solution.  
The only other libraries are related to the command line interface.

**Original Text and Link**: https://www.codewars.com/kata/525fbff0594da0665c0003a3

In this finite version of Conway's Game of Life: https://www.wikiwand.com/en/Conway%27s_Game_of_Life

The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead. Every cell interacts with its eight neighbors, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

- Any live cell with fewer than two live neighbors dies, as if caused by under-population.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies, as if by overcrowding.
- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed—births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick (in other words, each generation is a pure function of the preceding one)

## Project Setup

If you want to launch and debug the code on your machine please do:
```bash
#Install poetry on your python local machine versions
pip install poetry

#Inside the project: use poetry to install the libraries
poetry install

#Active the new poetry venv just created
poetry shell

#Launch the code
poetry run program.py
```

If you want to launch the project with some advance configuration (using typer on command line) you have to launch:
```bash

```

The advance parameters you can use are: 
- **rows**:
- **columns**:
- **max_prob**:
- **max_tick**:
- **time**: 
- **debug**: 