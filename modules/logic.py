# організувати фнцію для випадкового вибору незанятих клітинок
# механізм для статусу загаданого слова
from abc import ABC, abstractmethod, abstractproperty
import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init(self)
    # size
    height = 0
    weight = 0
    # position
    pos = []
    prev_pos = []

    color = None

class Chunk(Block):
    pos = [0, 0]
    prev_pos = [0, 0]
    color = "snake_tale_color"

    def __str__(self) -> str:
        return self.pos



class Wall(Block):
    color = "wall_color"

    def __init__(self, letter):
        super(Wall, self).__init__(self)
        self.letter = letter


class Food(Block):
    color = "food_colr"
    pos = []
    prev_pos = []

    def __init__(self, letter):
        self.letter = letter


class Head(Chunk):
    color = "head_snake_color"
    pos = [0, 0]
    prev_pos = []
    direction = "left"

    #  can be: left, right, up, down

    def __init__(self, letter):
        super(Head, self).__init__()
        self.letter = letter

    def move(self, key):
        if key == "up" and self.direction != 'down':
            self.prev_pos = self.pos
            self.pos[1] = self.pos[1] + 1  # move up y+1
            self.direction = 'up'
        if key == "down" and self.direction != 'up':
            self.prev_pos = self.pos
            self.pos[1] = self.pos[1] - 1  # move down y-1
            self.direction = 'down'
        if key == "left" and self.direction != 'right':
            self.prev_pos = self.pos
            self.pos[1] = self.pos[1] - 1  # move left x-1
            self.direction = 'left'
        if key == "right" and self.direction != 'left':
            self.prev_pos = self.pos
            self.pos[1] = self.pos[1] + 1  # move right x+1
            self.direction = 'right'

    def on_collision(self, other):
        pass

    def eat(self):
        pass

    def __str__(self) -> str:
        return self.pos + "__" + self.direction




class Table:
    def __init__(self, board_size, wall_count):
        self.board = board_size
        self.board = [[i for i in range(board_size)] for j in range(board_size)]
        self.head = Head('n')



    def on_won(self):
        pass

    def on_lose(self):
        pass

    def __str__(self):
        # bla = self.board[0][0]
        # return bla
        pass

class Snake(pygame.sprite.Group):
    def __init__(self):
        super().__init__(self)

    def turn(self, key):
        print(key)


if __name__ == "__main__":
    table = Table(1, 0)

