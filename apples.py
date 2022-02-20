from random import randint
from snake import Snake

class AppleState:
    SnakeShouldExtend = 0
    SnakeShouldNotExtend = 1

class Apples:
    def __init__(self, grid_dims):
        self.apple_locations = set()
        self.grid_dims = grid_dims

    def spawn(self):
        next_location = (randint(0, self.grid_dims[0] - 1), randint(0, self.grid_dims[1] - 1))
        self.apple_locations.add(next_location)

    def tick(self, snake: Snake):
        if snake.head() in self.apple_locations:
            self.apple_locations.remove(snake.head())
            self.spawn()

            return AppleState.SnakeShouldExtend

        return AppleState.SnakeShouldNotExtend