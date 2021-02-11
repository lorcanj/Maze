
class Distances:

    def __init__(self, root):
        self.root = root
        self.cells = {}
        self.cells[root] = 0

    def return_distance(self, cell):
        return self.cells.get(cell)
    
    def record_distance(self, cell, distance):
        self.cells[cell] = distance
    
    def return_cells(self):
        return self.cells.keys