import os
import sys
import math
import json

import pygame
from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT, QUIT, KEYDOWN

from modules.logic import Snake
import modules.frame

###### CONSTANTS ######
BLOCK_SIZE = [50, 50]
DISPLAY_SIZE = [500, 500]
BLACK = (0, 0, 0)

#Pygame initialization
pygame.init()
screen = pygame.display.set_mode(DISPLAY_SIZE)
snake = Snake()

def main():
    while True:
        # Main loop
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == KEYDOWN and e.key == K_UP:
                snake.turn(e.key)
            if e.type == KEYDOWN and e.key == K_DOWN:
                snake.turn(e.key)
            if e.type == KEYDOWN and e.key == K_LEFT:
                snake.turn(e.key)
            if e.type == KEYDOWN and e.key == K_RIGHT:
                snake.turn(e.key)

        screen.fill(BLACK)
        pygame.display.flip()


if __name__ == "__main__":
    main()
