import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, player, game):
        super().__init__()
        self.player = player
        self.game = game
        self.image = pygame.image.load('assets/bullet.png')
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 16
        self.rect.y = player.rect.y
        self.velocity = 2

        self.originImage = self.image
        self.angle = 0

        self.i = 0

    def rotate(self):
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.originImage, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self):

        if not self.game.checkCollision(self, self.game.allUfo):

            self.rect.y -= self.velocity
            self.rotate()

            if self.rect.y < -32:
                # permet la suppresion des balles à la sortie de l'écran
                self.player.allBullet.remove(self)
        else:
            self.game.score += 1
            self.player.allBullet.remove(self)