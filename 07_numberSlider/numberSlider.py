# Number Slider, by Marcus Brunson, based on project by Al Sweigart, v0.1

import sys, random, pygame
# sys module provides access to system resources (i,e. Operating System Commands)

from pygame.locals import *
# Allows us to call functions from pygame using just the function name instead of module.function()
# Example: We can use draw() instead of pygame.draw()

# Constants for Game Broad 
BOARDWIDTH = 4 # Columns 
BOARDHEIGHT = 4 # ROWS
TITLESIZE = 80 # Measured in Pixels 
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FPS = 30
BLANK = None
