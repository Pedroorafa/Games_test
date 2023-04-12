import pygame, sys

pygame.init()

width = 500
height = 500
cor_branca = (255, 255, 255)

screnn = pygame.display.set_mode((width, height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screnn.fill(cor_branca)
    pygame.display.update()
