# Final Project, Marcus Brunson, v0.0
import random, pygame
from sys import exit  

resolution = 0 # 0 = Low Resolution (800, 600), 1 = High Resolution (1920, 1080)

if resolution == 0:
    x = 800
    y = 600 
else:
    x = 1920 
    y = 1080


difficulty = int(input("Please choose a difficulty. Enter 1 for Easy or 2 for HARD.\n"))

if difficulty == 1:
    pygame.display.set_caption('NAME OF GAME -- EASY')
else: 
    pygame.display.set_caption('NAME OF GAME -- HARD') 

    # Colors 
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

pygame.init() 
screen = pygame.display.set_mode((x, y))  
pygame.display.set_caption('MARCUS Golden Axe -- EASY')
pygame.display.set_caption('MARCUS Golden Axe -- HARD') 
clock = pygame.time.Clock() 

sky_surface = pygame.image.load('img/ultimatePygame/Sky.png').convert()
ground_surface = pygame.image.load('img/ultimatePygame/ground.png').convert()

demon_surface = pygame.image.load('img/ultimatePygame/04_FuryDemon.png').convert_alpha()
demon_rect = demon_surface.get_rect(bottomright = (600,300))

player_surface = pygame.image.load('img/ultimatePygame/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0


game_active = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    demon_rect.left = 800

    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))

    pygame.display.update()
    clock.tick(60) 

    # player_image = pygame.image.load().convert()
    # enemy_image = pygame.image.load().convert()
    background_image = pygame.image.load('img/ultimatePygame/Sky.png').convert()


