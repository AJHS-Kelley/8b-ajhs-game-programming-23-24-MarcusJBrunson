# Final Project, Marcus Brunson, v0.0
import random
import pygame 
from sys import exit  

resolution = 0  # 0 = Low Resolution (800, 600), 1 = High Resolution (1920, 1080)
resolution = int(input("Please choose resolution. Enter 0 for low res or 1 for high.\n"))

if resolution == 0:
    x = 800
    y = 600 
else:
    x = 1920 
    y = 1080

# Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0) 

# Variables 
enemy_health = 100
player_health = 100
# player_damage = random.randint
# magic_attack = random.randit
                 
difficulty = int(input("Please choose a difficulty. Enter 1 for Easy or 2 for HARD.\n")) 

if difficulty == 1:
    pygame.display.set_caption('NAME OF GAME -- EASY')
    enemy_health = 100 
    player_health = 100
    # player_damage = random.randint
    # Magic_attack = random.randit 
else: 
    pygame.display.set_caption('NAME OF GAME -- HARD') 
    # enemy_health = 100 
    # player_health = 100
    # player_damage = random.randint
    # magic_attack = random.randit 

# Intitalize Pygame
pygame.init()

# Create the Screen 
screen = pygame.display.set_mode((x, y)) 
pygame.display.set_caption('MARCUS Golden Axe -- EASY')
pygame.display.set_caption('MARCUS Golden Axe -- HARD') 
clock = pygame.time.Clock() 

# Load Images
sky_surface = pygame.image.load('img/ultimatePygame/Sky.png').convert()
ground_surface = pygame.image.load('img/ultimatePygame/ground.png').convert()

# snail_surface = pygame.image.load('img/ultimatePygame/snail1.png').convert_alpha()
# snail_rect = snail_surface.get_rect(bottomright = (600,300))

player_surface = pygame.image.load('img/ultimatePygame/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0

game_active = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # if game_active:
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
        #             player_gravity = -20
            
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
        #             player_gravity = -20
        #     else:
        #         if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #             game_active = True
        #             snail_rect.left = 800

    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))

        # snail_rect.x -= 4
        # if snail_rect.right <= 0: snail_rect.left = 800
        # screen.blit(snail_surface,snail_rect)

        # Player
        player_gravity += 1
        # player_rect.y = player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surface,player_rect) 

        # Controls:
        # Mouse RIGHT-ARROW -- MOVE FORWARD 
        # MOUSE LEFT-ARROW -- MOVE BACKWARD 
        # MOUSE A KEY, Press -- Magic 
        # MOUSE D KEY, Press -- ATTACK
        # MOUSE F KEY, Press -- JUMP   

        # collision 
        # if snail_rect.colliderect(player_rect):
        #     game_active = False
        #  else:
        #       screen.fill('Yellow')

    pygame.display.update()
    clock.tick(75)




