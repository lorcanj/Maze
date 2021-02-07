
class Distances:

    def __init__(self, root):
        self.root = root
        self.cells = {}
        self.cells[self.root] = 0

    def