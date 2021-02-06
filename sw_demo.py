from Grid import Grid
from Sidewinder import Sidewinder

grid = Grid(20, 25)
Sidewinder.on_update(grid)
print(str(grid))