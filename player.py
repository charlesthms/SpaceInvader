import pygame

from bullet import Bullet


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('assets/player2.png')
        self.rect = self.image.get_rect()
        self.rect.x = 370
        self.rect.y = 530
        self.velocity = 2

        self.hs = self.read_HS()

        self.font = pygame.font.Font('assets/font/game_over.ttf', 150)

        self.allBullet = pygame.sprite.Group()
        self.stop = False

    def checkgame(self):
        if self.game.checkCollision(self, self.game.allUfo):

            if int(self.game.score) > self.hs:
                self.write_HS(self.game.score)

            self.gameover()
            self.stop = True

        elif len(self.game.allUfo) == 0:

            if int(self.game.score) > self.hs:
                self.write_HS(self.game.score)

            print('Fin du niveau.')
            self.stop = True

    def launchBullet(self):
        self.allBullet.add(Bullet(self, self.game))

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def gameover(self):

        gameOverMenu = pygame.image.load('assets/menus/gameover.jpg')
        self.game.screen.blit(gameOverMenu, (0, 0))
        self.game.screen.blit(self.font.render("Score : " + str(self.game.score), True, (147, 66, 245)), (285, 150))
        pygame.display.update()
        pygame.time.delay(5000)

    def read_HS(self):

        try:
            file = open("data/HS.txt", 'r')
            high_score = int(file.read())
            file.close()

            print('High score : ', high_score)

            return high_score

        except IOError:
            print('No high score yet.')


    def write_HS(self, new_hs):

        try:
            file = open("data/HS.txt", "w")
            file.write(str(new_hs))
            file.close()

        except IOError:
            print('Erreur de sauvegarde du score.')
