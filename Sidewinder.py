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
            
            
            #this is a a test
            
