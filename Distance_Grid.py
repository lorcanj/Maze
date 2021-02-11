from util import base36
from Grid import Grid

class Distance_Grid(Grid):

    def __init__(self, rows, columns):
        super().__init__(rows, columns)
        self.distances = None

    def set_distance(self, distance):
        self.distances = distance

    def get_distance(self):
        return self.distances
    # need something to set the value of the distances here
    # i.e. you need to add your getters and setters because they are done in one line in ruby

    def contents_of(self, cell):
        #if self.return_distance(linked) is None
        #and self.distances[cell]
        if self.get_distance() is not None:
            return str(self.get_distance().return_distance(cell))
        else:
            return super().contents_of(cell)
            
            