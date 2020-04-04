# організувати фнцію для випадкового вибору незанятих клітинок
# механізм для статусу загаданого слова
import math
import pygame
from pygame.sprite import Sprite, Group, GroupSingle

from .constants import BLOCK_SIZE, GREEN, RED, BLACK, BLUE
from .logic import get_free_cell
from pygame import (K_UP, K_DOWN, K_LEFT,
                    K_RIGHT, QUIT, KEYDOWN)


class World():
    def __init__(self):
        super().__init__()
        self.groups = [
                        Snake(self),
                        Foods(self),
                        Enemies(self)
                        ]

        self.snake = self.groups[0]

    def update(self):
        [group.update() for group in self.groups]
        
        sprites =  list()
        [sprites.extend(group.sprites()) for group in self.groups]
        self.positions = [sprite.rect.topleft for sprite in sprites]

    def draw(self, screen):
        [group.draw(screen) for group in self.groups]


class Foods(GroupSingle):
    def __init__(self, world):
        super().__init__()
        self.world = world
        self.add(Food((300, 300)))


class Enemies(Group):
    def __init__(self, world):
        super().__init__()
        self.world = world


class Snake(Group):
    def __init__(self, world):
        super().__init__()
        self.world = world
        self.__direction = 0
        self.__turn_pool = list()
        self.head = Head()
        self.head.rect.topleft = (0, 0)
        self.add(self.head)
        self.growth(3)
        
    @property
    def direction(self):
        if self.__turn_pool:
            self.__direction = self.__turn_pool.pop(0)

        return self.__direction

    @direction.setter
    def direction(self, value):
        self.__turn_pool.append(value)

    def growth(self, lenght=1):
        for each in range(lenght):
            tail = Tail()
            self.add(tail)

    def turn(self, key):
        if self.__direction != math.pi and key == K_UP:
            self.direction = math.pi
        elif self.__direction != 0 and key == K_DOWN:
            self.direction = 0
        elif self.__direction != math.pi*1/2 and key == K_LEFT:
            self.direction = math.pi * 3 / 2
        elif self.__direction != math.pi*3/2 and key == K_RIGHT:
            self.direction = math.pi * 1 / 2
    
    def update(self):
        # Fetch from pool direction
        direction = self.direction
        # Create temporary variable to store the move next place coord
        placeholder = self.head.rect.move(  (BLOCK_SIZE[0]) * \
                                            math.sin(direction),\
                                            (BLOCK_SIZE[1]) * \
                                            math.cos(direction) )
        # Calculate first placeholder for head only
        placeholder = placeholder.topleft
        # Update the Body
        sprites = self.sprites()
        for i in range(len(sprites)): # A = B B = T T = A
            sprites[i].rect.topleft, placeholder = placeholder, sprites[i].rect.topleft


class Block(Sprite):
    def __init__(self, pos=(-100, -100)):
        super().__init__()
        self.image = pygame.Surface(BLOCK_SIZE)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos


class Chunk(Block):
    def __init__(self):
        super().__init__()


class Wall(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.image.fill(BLACK)


class Food(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.image.fill(GREEN)


class Head(Chunk):
    def __init__(self):
        super().__init__()
        self.image.fill(RED)


class Tail(Chunk):
    def __init__(self):
        super().__init__()
        self.image.fill(BLUE)


