class Game:
    def __init__(self, state):
        self.state = state

    def is_cell_alive(self, x, y):
        alive_neighbours = self.count_alive_neighbors(x, y)
        return alive_neighbours == 3 or (self.state[x][y] == 1 and alive_neighbours == 2)

    def count_alive_neighbors(self, x, y):
        alive_neighbours = 0
        if x - 1 >= 0 and y - 1 >= 0:
            alive_neighbours += self.state[x - 1][y - 1]

        if x - 1 >= 0:
            alive_neighbours += self.state[x - 1][y]

        if x - 1 >= 0 and y + 1 < len(self.state[0]):
            alive_neighbours += self.state[x - 1][y + 1]

        if y - 1 >= 0:
            alive_neighbours += self.state[x][y - 1]

        if y + 1 < len(self.state[0]):
            alive_neighbours += self.state[x][y + 1]

        if x + 1 < len(self.state) and y - 1 >= 0:
            alive_neighbours += self.state[x + 1][y - 1]

        if x + 1 < len(self.state):
            alive_neighbours += self.state[x + 1][y]

        if x + 1 < len(self.state) and y + 1 < len(self.state[0]):
            alive_neighbours += self.state[x + 1][y + 1]

        return alive_neighbours
