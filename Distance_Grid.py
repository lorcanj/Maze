from util import *
from Grid import Grid

class Distance_Grid(Grid):

    def __init__(self, rows, columns):
        super().__init__(rows, columns)
        self.distances = None

    
    # need something to set the value of the distances here
    # i.e. you need to add your getters and setters because they are done in one line in ruby

    def contents_of(self, cell):
        #if self.return_distance(linked) is None
        #and self.distances[cell]
        if self.distances and self.:
            str(base36.base36encode(self.distances[cell]))
        else:
            super().contents_of(cell)
            
            