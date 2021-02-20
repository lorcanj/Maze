from Distance_Grid import Distance_Grid
from Binary_tree import BinaryTree

grid = Distance_Grid(5, 5)
BinaryTree.on(grid)

start = grid.plane_grid[0][0]

distance = start.distances()

grid.set_distance(distance)

#print(str(grid))

new_start = distance.longest_path()

new_distances = new_start.distances()

grid.set_distance(new_distances)

#print(str(grid))

goal = new_distances.longest_path()

grid.distances = new_distances.path_to(goal, new_start)

print(str(grid))
