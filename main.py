import pygame
from pygame.locals import *
from sys import exit
from sight import *
from bg_handler import *
from npc_handler import *
from player import *
from enemy import *
from utils import *

class Game:
    def __init__(self):
        #inicializa componentes do pygame
        pygame.init()
        #dimensões da tela (definidas em utils.py)
        self.width = screen_width
        self.height = screen_height
        #define layout e titulo do game
        self.janela = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Game TEST')
        #controle de cenário, npcs e player
        self.current_scenario = 1
        self.npcs = NPC_Handler(self)
        self.player = Player(self.janela)
        self.enemy = Enemy(self.janela)
        #imagens
        self.sprites = pygame.sprite.Group()
        self.sight = Sight(self.janela)
        self.background = BGHandler(self.janela)
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
                # Troca de cenario
                if(keys[pygame.K_LEFT]):
                    self.current_scenario -= 1
                if(keys[pygame.K_RIGHT]):
                    self.current_scenario += 1
                # Controle de indices maximo e minimo do cenario
                if(self.current_scenario < 1):
                    self.current_scenario = 1
                elif(self.current_scenario > ( len(self.background.backgrounds) - 1) ):
                    self.current_scenario = len( self.background.backgrounds ) - 1        
        self.sprites.update()
        self.background.update( self.current_scenario )
        self.player.update( self.background.get_floor_rect() )
        self.enemy.update( self.background.get_floor_rect(), self.player )
        self.npcs.update( self.current_scenario, self.player )
        pygame.display.update()
    #================================================================
    def draw(self):
        self.background.draw()
        self.player.draw()
        self.enemy.draw()
        self.npcs.draw()
        self.sprites.draw(self.janela)
        self.sight.draw()    
    #================================================================ 
    def menu_loop(self):
        self.background.update(0)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()  
                if(keys[pygame.K_RETURN]):
                    self.game_paused = False
                    #self.current_scenario = 1
                elif(keys[pygame.K_ESCAPE]):
                    pygame.quit()
                    exit()
                    
        self.background.draw()
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