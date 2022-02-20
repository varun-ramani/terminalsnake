from enum import Enum
from collections import deque

class Direction:
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP = (0, -1)
    DOWN = (0, 1)

class Snake:
    def __init__(self, initial_coord, direction):
        self.direction = direction
        self.positions = deque([initial_coord])

    def tick(self):
        head_x, head_y = self.head()

        dx, dy = self.direction
        next_x, next_y = head_x + dx, head_y + dy

        self.positions.append((next_x, next_y))
        self.positions.popleft()

    def extend(self):
        tail = self.tail()
        self.tick()
        self.positions.appendleft(tail)

    def set_direction(self, new_direction):
        self.direction = new_direction

    def head(self):
        return self.positions[-1]

    def tail(self):
        return self.positions[0]