import pygame
from pygame.locals import *
from sys import exit
from sight import Sight
from level_controller import *
from consts import *
from utils import *

class Game:
    def __init__(self):
        # inicializa componentes do pygame
        pygame.init()
        # dimensões da tela (definidas em utils.py)
        self.width = screen_width
        self.height = screen_height
        # define layout e titulo do game
        self.janela = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Game TEST')
        # configura as cenas do jogo
        self.curr_level = 0
        self.levels = []
        self.load_levels()
        # imagens
        self.sprites = pygame.sprite.Group()
        self.sight = Sight(self.janela)
        pygame.mouse.set_visible(False)
        self.game_paused = True
    #================================================================
    def update(self):
        #fecha o jogo se clicar no 'x'
        for event in pygame.event.get():
            self.sight.update(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                # retorna para menu
                if(keys[pygame.K_ESCAPE]):
                   self.game_paused = True    
        self.sprites.update()
        self.levels[self.curr_level].update()
        pygame.display.update()
    #================================================================
    def draw(self):
        self.levels[self.curr_level].draw()
        self.sprites.draw(self.janela)
        self.sight.draw() 
    #================================================================   
    def load_levels(self):
        self.levels.append( Level(self, MAINMENU) )
        self.levels.append( Level(self, MCBEDROOM) )
    #================================================================ 
    def menu_loop(self):
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()  
                if(keys[pygame.K_RETURN]):
                    self.game_paused = False
                    self.curr_level = 1
                elif(keys[pygame.K_ESCAPE]):
                    pygame.quit()
                    exit()
        self.levels[0].update()
        self.levels[0].draw()
    #================================================================
    def run(self):
        while True:
            if(self.game_paused is True):
                self.menu_loop()
            else:
                self.update()
                self.draw()
#====================================================================
if __name__ == '__main__':
    game = Game()
    game.run()