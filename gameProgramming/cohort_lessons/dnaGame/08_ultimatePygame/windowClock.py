import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
Clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

sky_surface = pygame.image.load('img/ultimatePygame/Sky.png').convert()
ground_surface = pygame.image.load('img/ultimatePygame/ground.png').convert()
text_surface = test_font.render('My game', False, 'Green')

snail_surface = pygame.image.load('img/ultimatePygame/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600,300))

player_surface = pygame.image.load('img/ultimatePygame/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))


    screen.blit(snail_surface,snail_rect)
    screen.blit(player_surface,player_rect)

    pygame.display.update()
    Clock.tick(60)