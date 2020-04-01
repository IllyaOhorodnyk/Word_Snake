import os
import sys
import math
import json

import pygame
from pygame import (K_UP, K_DOWN, K_LEFT,
                    K_RIGHT, QUIT, KEYDOWN)

from modules.frame import Snake

###### CONSTANTS ######
from modules.constants import (BLOCK_SIZE, DISPLAY_SIZE, RED,
                               GREEN, BLUE, BLACK, WHITE)

#Pygame initialization
pygame.init()
screen = pygame.display.set_mode(DISPLAY_SIZE)
snake = Snake()

def main():
    clock = pygame.time.Clock()
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

        clock.tick(4)
        screen.fill(WHITE)
        snake.update()
        snake.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
