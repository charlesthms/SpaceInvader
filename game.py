import pygame
import random

from player import Player
from ufo import Ufo


class Game():

    def __init__(self, menu):

        self.screen = pygame.display.set_mode((800, 600))
        self.background = pygame.image.load('assets/gameBg.jpg')

        self.menu = menu

        self.difficulty_str = self.menu.difficulty_str

        self.player = Player(self)
        self.pressed = {}
        self.allUfo = pygame.sprite.Group()
        self.spawn_ufo()
        self.score = 0
        self.font = pygame.font.Font('assets/font/game_over.ttf', 64)
        self.shoot_sound = pygame.mixer.Sound('assets/sounds/tir.ogg')
        self.shoot_sound.set_volume(0.2)
        self.click = False

        self.hight_score = 0

        self.gameLoop()

    def spawn_ufo(self):
        for i in range(1, Ufo(self).spawn_rate):
            ufo = Ufo(self)
            self.allUfo.add(ufo)

    def respawn(self):
        self.allUfo.add(Ufo(self))

    def checkCollision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, True, pygame.sprite.collide_mask)

    def gameLoop(self):

        loop = self.player.stop

        while not loop:

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.font.render("Score : " + str(self.score), True, (156, 232, 255)), (0, 0))
            self.screen.blit(self.player.image, self.player.rect)

            for bullet in self.player.allBullet:
                bullet.move()

            for ufo in self.allUfo:
                ufo.move()

            self.player.allBullet.draw(self.screen)
            self.allUfo.draw(self.screen)

            if self.pressed.get(pygame.K_d) and self.player.rect.x + self.player.image.get_width() < 800:
                self.player.move_right()
            elif self.pressed.get(pygame.K_a) and self.player.rect.x > 0:
                self.player.move_left()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False

                if event.type == pygame.KEYDOWN:
                    self.pressed[event.key] = True

                    if event.key == pygame.K_ESCAPE:
                        self.pauseMenu()

                elif event.type == pygame.KEYUP:
                    self.pressed[event.key] = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.player.launchBullet()
                    self.shoot_sound.play()

            self.player.checkgame()
            loop = self.player.stop
            pygame.display.update()

    def pauseMenu(self):

        background = pygame.image.load('assets/menus/pauseBg.png')
        menu = pygame.image.load('assets/menus/menu.png')
        menuOver = pygame.image.load('assets/menus/menuOver.png')

        click = pygame.mixer.Sound('assets/sounds/click.ogg')
        click.set_volume(0.2)

        loop = True
        click_on_resume = False

        while loop:

            self.screen.blit(background, (0, 0))
            self.screen.blit(menu, (300, 400))

            mx, my = pygame.mouse.get_pos()

            button_menu = menu.get_rect()
            button_menu.x, button_menu.y = 300, 400

            if button_menu.collidepoint((mx, my)):
                self.screen.blit(menuOver, (300, 400))
                pygame.display.update()
                if self.click:
                    click.play()
                    loop = False
                    self.menu.__init__()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.click = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or click_on_resume is True:
                        loop = False

            pygame.display.update()



