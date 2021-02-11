from Distances import Distances


class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.links = {}
    
    def link(self, cell, bidi=True):
        self.links[cell] = True
        if bidi:
            cell.link(self, False)
        return self
        
    def unlink(self, cell, bidi=True):
        self.links.pop(cell, None)
        if bidi:
            cell.unlink(self, False)
        return self

    def links(self):
        return list(self.links.keys())

    def is_linked(self, cell):
        if not cell:
            return False
        # might need to check this
        if cell in self.links:
            return True
        return False
        #return self.links.get(cell)

    def neighbours(self):
        list_of_neighbours = []
        if north:
            list_of_neighbours.append(north)
        if south:
            list_of_neighbours.append(south)
        if east:
            list_of_neighbours.append(east)
        if west:
            list_of_neighbours.append(west)
        return list_of_neighbours

    def distances(self):
        # need to update this as linked is not currently being picked up as anything
        distances = Distances(self)
        frontier = [self]

        while any(frontier):
            new_frontier = []

            for cell in frontier:
                for linked in cell.links:
                    if distances.return_distance(linked) is None and distances.return_distance(cell) is not None:
                        distances.record_distance(linked, distances.return_distance(cell) + 1)
                        new_frontier.append(linked)
            frontier = new_frontier
        
        return distances

