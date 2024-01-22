# Number Slider, by Marcus Brunson, based on project by Al Sweigart, v0.2

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
FPS = 30 # This is a maxiumum value! Won't make a slow computer run faster.
BLANK = None

# Color VALUES in (R, G, B) format.
# 0 = No value, 255 = Max Value 
Black = (0, 0, 0) 
WHITE = (255, 255, 255)
BRIGHTBLUE = (0, 50, 225)
DARKTURQUOISE = (3, 54, 73)
GREEN = (0, 204, 0)

# Broad Design Setup 
BGCOLOR = DARKTURQUOISE
TITLECOLOR = GREEN 
TEXTCOLOR = WHITE 
BROADCOLOR = BRIGHTBLUE
BASICFONTSIZE = 20 # PIXELS

# Button setup 
BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = Black
MESSAGECOLOR = WHITE 