from Cell import Cell
import random

class Grid:


    def prepare_grid(self):
        matrix = [[0]* self.columns] * self.rows
        for i in range(self.rows - 1):
            for j in range(self.columns - 1):
                matrix[i][j] = Cell(i, j)
        return matrix

    def configure_cells(self):
        for cell in self.plane_grid:
            row, col = cell.row, cell.column
            
            cell.north = self[row - 1, col]
            cell.south = self[row + 1, col]
            cell.west = self[row, col - 1]
            cell.east = self[row, col + 1]

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.plane_grid = self.prepare_grid()
        self.configure_cells() 

    
    
    def check_cell(row, column):
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

    def each_row(self):
        for row in self.rows:
            yield self.plane_grid[row]

    def each_cell(self):
        for row in self.rows:
            for column in self.columns:
                if cell:
                    yield cell
    

        