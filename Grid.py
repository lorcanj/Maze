from Cell import Cell
import random
from PIL import Image, ImageDraw
import png

class Grid:
    
    def contents_of(self, cell):
        return "  "

    def __str__(self):
        output = "+" + "---+" * self.columns + "\n"

        for row in self.each_row():
            top = "|"
            bottom = "+"

            for cell in row:
                if not cell:
                    cell = Cell(-1, 1)
                body = self.contents_of(cell)
                if cell.is_linked(cell.east):
                    east_boundary = " "
                else:
                    east_boundary = "|"
                body += east_boundary
                top += body

                if cell.is_linked(cell.south):
                    south_boundary = "   "
                else:
                    south_boundary = "---"
                corner = "+"
                south_boundary += corner
                bottom += south_boundary
            
            top += "\n"
            output += top

            bottom += "\n"
            output += bottom

        return output

    def to_png(self, cell_size=10):
        # need to complete this once have found a good library for pngs
        img_width = cell_size * self.columns
        img_height = cell_size * self.rows

        background = (0,0,0)
        wall = (255,255,255)

        img = Image.new("RGB", (img_width + 1, img_height + 1), background)

        draw = ImageDraw.Draw(img)

        for cell in self.each_cell():
            x1 = cell.column * cell_size
            y1 = cell.row * cell_size

            x2 = (cell.column + 1) * cell_size
            y2 = (cell.column + 1) * cell_size

            if not cell.north:
                draw.line([(x1,y1), (x2, y1)], wall, 1)
            
            if not cell.west:
                draw.line([(x1, y1), (x1, y2)], wall, 1)
            
            if not cell.is_linked(cell.east):
                draw.line([(x2, y1), (x2, y2)], wall, 1)

            if not cell.is_linked(cell.south):
                draw.line([(x1, y2), (x2, y2)], wall, 1)
                
        return img


    def each_row(self):
        for row in range(self.rows):
            yield self.plane_grid[row]

    def each_cell(self):
        for row in self.each_row():
            for cell in row:
                yield cell

    def prepare_grid(self):
        
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


    

        