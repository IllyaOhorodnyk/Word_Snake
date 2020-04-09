# організувати фнцію для випадкового вибору незанятих клітинок
# механізм для статусу загаданого слова
import math
import pdb
import random
import pygame
import sys
import json
from pygame.sprite import Sprite, Group, GroupSingle

from .constants import DISPLAY_SIZE, BLOCK_SIZE, GREEN, RED, BLACK, BLUE
from pygame import (K_UP, K_DOWN, K_LEFT,
                    K_RIGHT, QUIT, KEYDOWN)


class World():
    def __init__(self):
        super().__init__()
        self.all_positions = set()
        for x in range(0, DISPLAY_SIZE[0], BLOCK_SIZE[0]):
            for y in range(0, DISPLAY_SIZE[1], BLOCK_SIZE[1]):
                self.all_positions.add((x, y))

        self.word = choose_word("words.json")
        
        self.font = pygame.font.Font("miroslav.ttf", 28)
        surf = self.font.render(self.word[1], True, BLACK)
        sprite = pygame.sprite.Sprite()
        sprite.image = surf
        sprite.rect = surf.get_rect()
        sprite.rect.topleft = BLOCK_SIZE

        self.length = 3

        self.groups = list()

        self.groups.append(Enemies(self))
        self.enemies = self.groups[0]

        self.groups.append(Foods(self))
        self.foods = self.groups[1]

        self.groups.append(Snake(self))
        self.snake = self.groups[2]

        self.groups.append(pygame.sprite.GroupSingle(sprite))

    def update(self):
        [group.update() for group in self.groups]

        if self.snake.head.rect.topleft == self.foods.food.rect.topleft:
            self.snake.growth()
            self.foods.repoint()
        
        if self.snake.head.rect.topleft in \
                [each.rect.topleft for each in self.enemies.sprites()]:
            print("Game Over!")
            sys.exit(0)

    def draw(self, screen):
        [group.draw(screen) for group in self.groups]

    def get_free_cell(self):
        sprites =  list()
        [sprites.extend(group.sprites()) for group in self.groups]
        positions = set((sprite.rect.topleft for sprite in sprites))

        return random.choice(list(self.all_positions - positions))


class Foods(GroupSingle):
    def __init__(self, world):
        super().__init__()
        self.world = world
        self.food = Food(self.world.get_free_cell())
        surf = self.world.font.render(\
                self.world.word[0][self.world.length], True, BLACK)
        self.food.image.blit(surf, (0, 0))
        self.add(self.food)

    def repoint(self):
        self.food.image.fill(GREEN)
        surf = self.world.font.render(\
                self.world.word[0][len(self.world.snake)-1], True, BLACK)
        self.food.image.blit(surf, (0, 0))
        self.food.rect.topleft = self.world.get_free_cell()


class Enemies(Group):
    def __init__(self, world):
        super().__init__()
        self.world = world
        for i in range(0, DISPLAY_SIZE[0], BLOCK_SIZE[0]):
            self.add(Wall((0, i)))
            self.add(Wall((i, 0)))
            self.add(Wall((i, DISPLAY_SIZE[0]-BLOCK_SIZE[0])))
            self.add(Wall((DISPLAY_SIZE[1]-BLOCK_SIZE[1], i)))

        for i in range(self.world.length):
            self.add(Poison(self.world.get_free_cell()))

class Snake(Group):
    def __init__(self, world):
        super().__init__()
        self.world = world
        self.__direction = 0
        self.__turn_pool = list()
        self.head = Head()
        self.head.rect.topleft = self.world.get_free_cell()
        self.add(self.head)
        self.growth(self.world.length)
        
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
            surf = self.world.font.render(\
                    self.world.word[0][len(self.sprites())-1], True, BLACK)
            tail.image.blit(surf, (0, 0))
            self.add(tail)
            self.world.enemies.add(tail)

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


class Poison(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.image.fill(BLUE)


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



def choose_word(filename):
    try:
        file = open(filename)
        words = json.loads(file.read())
        file.close()
    except FileNotFoundError as e:
        print("File not found by the name ", filename)
        
    word = random.choice(list(words.keys()))
    return word, words[word]
