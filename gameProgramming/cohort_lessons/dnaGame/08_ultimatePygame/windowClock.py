import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
Clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

sky_surface = pygame.image.load('img/ultimatePygame/Sky.png')
ground_surface = pygame.image.load('img/ultimatePygame/ground.png')
text_surface = test_font.render('My game', False, 'Green')

snail_surface = pygame.image.load('img/ultimatePygame/snail.png')
snail_x_pos = 600

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    screen.bilt(snail_surface,(snail_x_pos,250))

    pygame.display.update()
    Clock.tick(60)
