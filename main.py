import os
import sys
import math
import json
import pdb

import pygame
from pygame import (K_UP, K_DOWN, K_LEFT, K_SPACE,
                    K_RIGHT, QUIT, KEYDOWN, K_ESCAPE)

from modules.frame import World

###### CONSTANTS ######
from modules.constants import (BLOCK_SIZE, DISPLAY_SIZE, RED,
                               GREEN, BLUE, BLACK, WHITE)



def main():
    pygame.init()
    #screen = pygame.display.set_mode(DISPLAY_SIZE, flags=pygame.FULLSCREEN)
    screen = pygame.display.set_mode(DISPLAY_SIZE)
    clock = pygame.time.Clock()
    world = World()
    
    while True:
        # Main loop
        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                sys.exit()
            elif e.type == KEYDOWN and e.key == K_UP:
                world.snake.turn(e.key)
            elif e.type == KEYDOWN and e.key == K_DOWN:
                world.snake.turn(e.key)
            elif e.type == KEYDOWN and e.key == K_LEFT:
                world.snake.turn(e.key)
            elif e.type == KEYDOWN and e.key == K_RIGHT:
                world.snake.turn(e.key)
            elif e.type == KEYDOWN and e.key == K_SPACE:
                pdb.set_trace()

        clock.tick(4)
        screen.fill(WHITE)
        world.update()
        world.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
