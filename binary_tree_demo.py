from Grid import Grid
from Binary_tree import BinaryTree

grid = Grid(5, 5)
BinaryTree.on(grid)
print(str(grid))

img = grid.to_png()
img.save("maze.png")