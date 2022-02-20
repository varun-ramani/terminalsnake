from snake import Snake
from enum import Enum
from apples import Apples

class GridState(Enum):
    SnakeOutOfBounds = 0
    SnakeInBounds = 1

class Grid:
    def __init__(self, dims):
        print()
        print()
        self.dims = dims

    def init_grid(self):
        self.grid = [[' ' for _ in range(self.dims[0] + 2)] for _ in range(self.dims[1] + 2)]

        for y_value in range(0, self.dims[1] + 2):
            self.grid[y_value][0] = '█'
            self.grid[y_value][self.dims[1] + 1] = '█'

        for x_value in range(0, self.dims[0] + 2):
            self.grid[0][x_value] = '█'
            self.grid[self.dims[1] + 1][x_value] = '█'


    def print_grid(self):
        print('\n'.join([''.join(row) for row in self.grid]), end='', flush=True)
        print(f'\x1b[{self.dims[1] + 1}A\x1b[{self.dims[0] + 1}D', end='', flush=True)

    def check_bounds(self, snake: Snake):
        x, y = snake.head()
        if (x < 0 or y < 0
            or x >= self.dims[0] or y >= self.dims[1]):

            return False

        return True
    
    def tick(self, snake: Snake, apples: Apples):
        if not self.check_bounds(snake):
            return GridState.SnakeOutOfBounds

        self.init_grid()
        for x, y in apples.apple_locations:
            self.grid[y + 1][x + 1] = 'a'
        for x, y in snake.positions:
            self.grid[y + 1][x + 1] = 'b'
        self.print_grid()

        return GridState.SnakeInBounds