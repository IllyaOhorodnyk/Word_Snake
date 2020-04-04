import math
import os
import sys

#from .constants import BLOCK_SIZE as B_S
#from .constants import DISPLAY_SIZE as D_S
B_S = [50, 50]
D_S = [500, 500]

def get_free_cell(positions):
    print([x for x in range(0, D_S[0], B_S[0])])
    print([y for y in range(0, D_S[0], B_S[0])])


get_free_cell([(0, 25), (0, 0), (300, 300)])
