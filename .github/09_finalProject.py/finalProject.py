# Final Project, Marcus Brunson, v0.0
import random, pygame 

resolution = 0 # 0 = Low Resolution (800, 600), 1 = High Resolution (1920, 1080)

if resolution == 0:
    x = 800
    y = 600 
else:
    x = 1920 
    y = 1080

pygame.init()

difficulty = int(input("Please choose a difficulty. Enter 1 for Easy or 2 for HARD.\n"))

if difficulty == 1:
    pygame.display.set_caption('NAME OF GAME -- EASY')
else: 
    pygame.display.set_caption('NAME OF GAME -- HARD')

pygame.display.set_caption('MARCUS Golden Axe -- EASY')
pygame.display.set_caption('MARCUS Golden Axe -- HARD')
screen = pygame.display.set_mode((x, y))  
# CREATE AN IF / ELSE BLOCK TO SET THE RESOLUTION BASED ON THE VARIABLE ABOVE.

# Colors 
White = (255, 255, 255)
Black = (0, 0, 0)

player_image = pygame.image.load().convert()
enemy_image = pygame.image.load().convert()
background_image = pygame.image.load().convert()


