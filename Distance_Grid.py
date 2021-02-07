from util import *


class Distance_Grid(Grid):

    def __init__(self, distances):
        self.distances = distances

    def contents_of(self, cell):
        if self.distances and self.distances[cell]:
            str(base36.base36encode(self.distances[cell]))
        else:
            super()
            
            