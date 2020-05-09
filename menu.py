import pygame

from game import Game


class Menu:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.click = False

        self.high_score = self.read_HS()
        self.difficulty_str = 'easy'

        self.startMenu()

    def startMenu(self):

        background = pygame.image.load('assets/menus/menuBg.jpg')
        jouer = pygame.image.load('assets/menus/jouer.png')
        jouerOver = pygame.image.load('assets/menus/jouerOver.png')
        options = pygame.image.load('assets/menus/options.png')
        optionOver = pygame.image.load('assets/menus/optionOver.png')
        quitter = pygame.image.load('assets/menus/quitter.png')
        quitterOver = pygame.image.load('assets/menus/quitterOver.png')

        click = pygame.mixer.Sound('assets/sounds/click.ogg')
        click.set_volume(0.2)

        while True:

            self.screen.blit(background, (0, 0))
            self.screen.blit(jouer, (300, 250))
            self.screen.blit(options, (300, 325))
            self.screen.blit(quitter, (300, 400))

            mx, my = pygame.mouse.get_pos()

            button1 = jouer.get_rect()
            button1.x, button1.y = 300, 250

            button2 = options.get_rect()
            button2.x, button2.y = 300, 325

            button3 = quitter.get_rect()
            button3.x, button3.y = 300, 400

            if button1.collidepoint((mx, my)):

                self.screen.blit(jouerOver, (300, 250))
                pygame.display.update()

                if self.click:
                    click.play()
                    Game(self)
                    self.click = False
            elif button2.collidepoint((mx, my)):

                self.screen.blit(optionOver, (300, 325))
                pygame.display.update()

                if self.click:
                    click.play()
                    self.optionsMenu()
            elif button3.collidepoint((mx, my)):

                self.screen.blit(quitterOver, (300, 400))
                pygame.display.update()

                if self.click:
                    click.play()
                    pygame.quit()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.click = False

            pygame.display.update()

    def optionsMenu(self):

        background = pygame.image.load('assets/menus/optionsBg.jpg')
        retour = pygame.image.load('assets/menus/retour.png')
        retourOver = pygame.image.load('assets/menus/retourOver.png')

        easy = pygame.image.load('assets/menus/facile.png')
        medium = pygame.image.load('assets/menus/moyen.png')
        hard = pygame.image.load('assets/menus/hard.png')

        easyOver = pygame.image.load('assets/menus/facileOver.png')
        mediumOver = pygame.image.load('assets/menus/moyenOver.png')
        hardOver = pygame.image.load('assets/menus/hardOver.png')

        click = pygame.mixer.Sound('assets/sounds/click.ogg')
        click.set_volume(0.2)


        loop = True

        while loop:

            self.screen.blit(background, (0, 0))
            self.screen.blit(retour, (300, 475))

            self.screen.blit(easy, (300, 250))
            self.screen.blit(medium, (300, 325))
            self.screen.blit(hard, (300, 400))

            mx, my = pygame.mouse.get_pos()

            button_return = retour.get_rect()
            button_return.x = 300
            button_return.y = 475

            button_easy = retour.get_rect()
            button_easy.x = 300
            button_easy.y = 250

            button_medium = retour.get_rect()
            button_medium.x = 300
            button_medium.y = 325

            button_hard = retour.get_rect()
            button_hard.x = 300
            button_hard.y = 400

            if button_return.collidepoint((mx, my)):

                self.screen.blit(retourOver, (300, 475))
                pygame.display.update()

                if self.click:
                    click.play()
                    loop = False
                    self.__init__()

            elif button_easy.collidepoint((mx, my)):
                self.screen.blit(easyOver, (300, 250))
                pygame.display.update()

                if self.click:
                    click.play()
                    self.difficulty_str = 'easy'
                    print('easy')
                    loop = False
                    self.__init__()

            elif button_medium.collidepoint((mx, my)):
                self.screen.blit(mediumOver, (300, 325))
                pygame.display.update()

                if self.click:
                    pass

            elif button_hard.collidepoint((mx, my)):
                self.screen.blit(hardOver, (300, 400))
                pygame.display.update()

                if self.click:
                    pass

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.click = False

            pygame.display.update()

    def read_HS(self):

        try:
            file = open("data/HS.txt", 'r')
            high_score = int(file.read())
            file.close()
            self.hight_score = high_score

        except IOError:
            print('il faut jouer pour avoir un high score !')


