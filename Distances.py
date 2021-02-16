
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

    def path_to(self, goal):
        current = goal

        breadcrumbs = Distances(self.root)
        breadcrumbs.cells[current] = self.cells[current]
        
        while self.cells[current] != 0:

            for link in current.links:
                if self.cells[link] + 1 == self.cells[current]:
                    breadcrumbs.cells[link] = self.cells[link]
                    current = link
        
        return breadcrumbs

