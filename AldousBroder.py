from Grid import Grid


class AldousBroder:

    def on(grid):
        cell = grid.random_cell()
        unvisited = grid.size() - 1

        while unvisited > 0:
            neighbour = cell.random_neighbour()

            if not bool(neighbour.links):
                cell.link(neighbour)
                unvisited = unvisited -1
            
            cell = neighbour
        
        return grid
