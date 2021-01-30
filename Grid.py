import Cell

class Grid:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        
        self.Grid = prepare_grid()
        configure_cells()
    
    def prepare_grid(self):
        matrix = [rows][columns]
        for i in range(this.rows):
            for j in range(this.columns):
                matrix[i][j] = Cell(row, column)
        return self

    def configure_cells(self):
        for cell in matrix:
            row, col = cell.row, cell.column

            cell.north = self[row - 1, col]
            cell.south = self[row + 1, col]
            cell.west = self[row, col - 1]
            cell.east = self[row, col + 1]
    