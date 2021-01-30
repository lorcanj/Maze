class Cell:
    def __init__(self, row, column):
        this.row = row
        this.column = column
        this.links = {}
    
    def link(self, cell, bidi=True):
        this.links[cell] = True
        if bidi:
            cell.link(self, False)
        
    def unlink(self, cell, bidi=True):
        this.links.pop(cell, None)
        if bidi:
            cell.unlink(self, False)

    def links(self):
        this.links.keys

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