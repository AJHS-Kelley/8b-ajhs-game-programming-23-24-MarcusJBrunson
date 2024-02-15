import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
Clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

sky_surface = pygame.image.load('img/ultimatePygame/Sky.png').convert()
ground_surface = pygame.image.load('img/ultimatePygame/ground.png').convert()

score_surface = test_font.render('My game', False, 'Green')
score_rect = score_surface.get_rect(center = (400,50))


snail_surface = pygame.image.load('img/ultimatePygame/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600,300))

player_surface = pygame.image.load('img/ultimatePygame/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos): print('collision')

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    pygame.draw.rect(screen, 'Pink',score_rect)
    pygame.draw.rect(screen, 'Pink',score_rect,10)
    
    screen.blit(score_surface,(300,50))

    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surface,snail_rect)
    screen.blit(player_surface,player_rect)

    # if player_rect.colliderect(snail_rect):
    #     print('collision')

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

    
    pygame.display.update()
    Clock.tick(60)