from Grid import Grid
from AldousBroder import AldousBroder

grid = Grid(20, 20)
AldousBroder.on(grid)

filename = "aldous_broder.png"
grid.to_png().save(filename)

