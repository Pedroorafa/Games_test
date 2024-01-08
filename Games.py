import pygame, sys

pygame.init()

width = 500
height = 500
color_white = (255, 255, 255)
color_gray = (127, 127,127)
size_surface = (75, 75)

screnn = pygame.display.set_mode((width, height))

rectangle = pygame.Surface(size_surface)
rectangle2 = pygame.Surface(size_surface)

rocket = pygame.image.load('./imagens/Rocket.png').convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screnn.fill(color_gray)
    rectangle.fill('red')
    rectangle2.fill('blue')
    screnn.blit(rectangle, (50, 50))
    screnn.blit(rectangle2, (60, 60))
    screnn.blit(rocket, (100, 100))

    pygame.display.update()
