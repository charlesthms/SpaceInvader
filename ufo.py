import pygame
import random


class Ufo(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()

        self.game = game

        self.velocity = 3

        self.image = pygame.image.load('assets/ufo1.png')
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800)
        self.rect.y = random.randint(0, 100)

        self.dir = 'right'

        self.difficulty = {'easy': (25, 1),
                           'medium': (50, 2),
                           'hard': (100, 3)
                           }

        self.difficulty_str = self.game.difficulty_str
        self.spawn_rate, self.velocity = self.difficulty[self.difficulty_str]

    def right(self):
        self.rect.x += self.velocity

    def left(self):
        self.rect.x -= self.velocity

    def down(self):
        self.rect.y += 100

    def detection(self):

        if self.dir == 'right' and self.rect.x >= 800 - self.image.get_width():
            self.down()
            self.dir = 'left'

        if self.dir == 'left' and self.rect.x <= 0:
            self.down()
            self.dir = 'right'

    def move(self):

        self.detection()

        if self.dir == 'right':
            self.right()

        elif self.dir == 'left':
            self.left()