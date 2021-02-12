from Distance_Grid import Distance_Grid
from Binary_tree import BinaryTree
from Cell import Cell


grid = Distance_Grid(10, 10)
BinaryTree.on(grid)


start = grid.plane_grid[0][0]
#distances
#  finish writing the above
distance = start.distances()
grid.set_distance(distance)

print(str(grid))
