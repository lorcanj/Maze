from Grid import Grid
from Cell import Cell
from random import random
class BinaryTree:

    def on(grid):
        for cell in grid.each_cell():
            neighbours = []
            if cell.north:
                neighbours.append(cell.north)
            if cell.east:
                neighbours.append(cell.east)
            index = int(random() * len(neighbours))
            if len(neighbours) != 0:
                neighbour = neighbours[index]
            if neighbour:
                cell.link(neighbour)
        return grid
