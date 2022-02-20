from enum import Enum
from grid import Grid, GridState
from snake import Snake, Direction
from apples import AppleState, Apples

from time import sleep

import curses, time

from sound_system import Sound

class GameState(Enum):
    PLAYING = 0
    OVER = 1

class Game:
    def __init__(self, grid_dims, init_coord):
        self.grid = Grid(grid_dims)
        self.snake = Snake(init_coord, Direction.UP)
        self.state = GameState.PLAYING
        self.apples = Apples(grid_dims)
        self.sound_system = Sound()

        self.apples.spawn()

    def get_next_input(self, stdscr):
        stdscr.nodelay(True)
        return stdscr.getch()

    def tick(self):
        next_input = curses.wrapper(self.get_next_input)
        if next_input == 100:
            self.snake.set_direction(Direction.RIGHT)
        elif next_input == 115:
            self.snake.set_direction(Direction.DOWN)
        elif next_input == 97:
            self.snake.set_direction(Direction.LEFT)
        elif next_input == 119:
            self.snake.set_direction(Direction.UP)

        if self.grid.tick(self.snake, self.apples) == GridState.SnakeOutOfBounds:
            return GameState.OVER

        self.snake.tick()
        
        if self.apples.tick(self.snake) == AppleState.SnakeShouldExtend:
            self.snake.extend()
            self.sound_system.play_eat_apple()

        return GameState.PLAYING

    def play(self, tick=1):
        while True:
            next_tick_result = self.tick()
            if next_tick_result != GameState.PLAYING:
                print("Game over!")
                self.sound_system.play_game_over()
                return

            time.sleep(0.2)