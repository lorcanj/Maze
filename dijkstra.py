from Distance_Grid import Distance_Grid
from Binary_tree import BinaryTree
from Cell import Cell


grid = Distance_Grid(5, 5)
BinaryTree.on(grid)


start = grid.plane_grid[0][0]
distance = start.distances()
grid.set_distance(distance)

print(str(grid))

grid.distances = distance.path_to(grid.plane_grid[grid.rows - 1][0])

print(str(grid))