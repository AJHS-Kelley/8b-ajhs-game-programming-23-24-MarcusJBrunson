import pygame
from sys import exit

# Almost finished Marcus, let's get it done instead of trying to summon Blue Eyes White Dragon during class. 

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

sky_surface = pygame.image.load('img/ultimatePygame/Sky.png').convert()
ground_surface = pygame.image.load('img/ultimatePygame/ground.png').convert()

score_surface = test_font.render('My game', False, (64,64,64))
score_rect = score_surface.get_rect(center = (400,50))


snail_surface = pygame.image.load('img/ultimatePygame/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600,300))

player_surface = pygame.image.load('img/ultimatePygame/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                player_gravity = -20
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                player_gravity = -20


    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(score_surface,score_rect)
    pygame.draw.rect(screen, '#c0e8ec',score_rect)
    pygame.draw.rect(screen, '#c0e8ec',score_rect,10)


    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surface,snail_rect)

    # Player
    player_gravity += 1
    player_rect.y = player_gravity
    if player_rect.bottom >= 300: player_rect.bottom = 300
    screen.blit(player_surface,player_rect)

    # collision 
    if snail_rect.colliderect(player_rect):
        pygame.quit()
        exit()
        
    pygame.display.update()
    clock.tick(60)