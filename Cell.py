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
        return self.links.key(cell)

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