import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((1080,840),RESIZABLE)

# fond = pygame.image.load("background.jpg").convert()
# fenetre.blit(fond,(0,0))

color=(255,255,255)

pygame.draw.rect(fenetre,color,pygame.Rect(500,500,50,50),0)
pygame.display.flip()
continuer =1

while continuer:
    continuer =int(input())
