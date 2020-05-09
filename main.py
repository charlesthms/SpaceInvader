import pygame

from menu import Menu


pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()

# Setup
icon = pygame.image.load('assets/ufo1.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Space Invader')

menu = Menu()



