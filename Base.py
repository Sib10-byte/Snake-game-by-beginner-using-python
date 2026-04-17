import pygame
from pygame import K_RIGHT

x = pygame.init()

#window creation
gameWindow = pygame.display.set_mode((1200,500))
pygame.display.set_caption("Sibs game")

#game boolians
exit_game = False
game_over = True

#game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             exit_game = True


        if event.type == pygame.KEYDOWN:
             if event.key == K_RIGHT:
               print("Dabb gaya bhai ")
pygame.quit()
quit()
