from Cell import Cell
import random

class Grid:
    
    def each_row(self):
        for row in range(self.rows):
            yield self.plane_grid[row]

    def each_cell(self):
        for row in self.each_row():
            # the cell should be a Cell object and not an int!!!!
            for cell in row:
                yield cell

    def prepare_grid(self):
        # need to create an empty matrix which I then fill with cells NEED TO CHANGE THIS HERE
        
        return[[Cell(row, column) for column in range(self.columns)] for row in range(self.rows)]
        """
        # this would not work as the elements in the 2d list were not
        # being updated to the cell type
        matrix = [[0]* self.columns] * self.rows
        for i in range(self.columns - 1):
            for j in range(self.rows - 1):
                matrix[i][j] = Cell(i, j)
        return matrix
        """
    
    def configure_cells(self):
        for cell in self.each_cell():
            row = cell.row
            col = cell.column

            #could not define and use the method as shown in the ruby book with the
            # method name '[]'
            cell.north = self.check_cell(row - 1, col)
            cell.south = self.check_cell(row + 1, col)
            cell.west = self.check_cell(row, col - 1)
            cell.east = self.check_cell(row, col + 1)

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.plane_grid = self.prepare_grid()
        self.configure_cells() 

    def check_cell(self, row, column):
        if row < 0 or row > self.rows - 1:
            return None
        if column < 0 or column > self.columns - 1:
            return None
        return self.plane_grid[row][column]

    def random_cell(self):
        row = int(random() * self.rows)
        column = int(random() * self.columns)
        return self.plane_grid[row][column]

    def size(self):
        return self.rows * self.columns

    
    

        