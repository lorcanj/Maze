from Grid import Grid
from Cell import Cell
from random import random, randint

class Sidewinder:

    def on(grid):
        # 0 is tails
        # 1 is heads
        # might be problem with
        for cell in grid.each_cell():
            run = []
            #could do a while loop here for the coin_flips
            heads = False
            while not heads:
                if cell.east is None:
                    break
                coin_flip = randint(0,1)
                if coin_flip == 0:
                    run.append(cell.east)
                    
                    if cell.east is not None:
                        cell.link(cell.east)
                        cell = cell.east
                else:
                    heads = True
            if len(run) != 0:
                index = int(random() * len(run))
                random_cell = run[index]
                if random_cell and random_cell.north is not None:
                    random_cell.link(random_cell.north)
        return grid


    def on_update(grid):
        # 0 is tails
        # 1 is heads
        for row in grid.each_row():
            run = []

            for cell in row:
                run.append(cell)
                north_barrier = False
                east_barrier = False
                if cell.north is None:
                    north_barrier = True
                if cell.east is None:
                    east_barrier = True
                coin_flip = randint(0,1)

                if north_barrier and not east_barrier:
                    cell.link(cell.east)
                if east_barrier and not north_barrier:
                    cell.link(cell.north)
                    if len(run) > 1:
                        for i in range(len(run) - 1):
                            run[i].link(run[i].east)
                        run = []
                        break
                if coin_flip == 1:
                    if not east_barrier:
                        for i in range(len(run) - 1):
                            run[i].link(run[i].east)
                    if not north_barrier:
                        index = int(random() * len(run))
                        run[index].link(run[index].north)
                    run = []

        return grid
            
