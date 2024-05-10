import pygame
from pygame.locals import *
from sys import exit
from sight import *
from background import *
from npc_handler import *
from player import *
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
        #controle de cenário, npc e player
        self.current_scenario = 0
        self.npcs = NPC_Handler(self)
        self.player = Player(self.janela)
        #imagens
        self.sprites = pygame.sprite.Group()
        self.sight = Sight(self.janela)
        self.background = BackGround(self.janela)
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
                if(self.current_scenario < 0):
                    self.current_scenario = 0
                elif(self.current_scenario > ( len(self.background.bg) - 1) ):
                    self.current_scenario = len( self.background.bg ) - 1        
        self.sprites.update()
        self.player.update()
        self.background.update( self.current_scenario )
        self.npcs.update( self.current_scenario, self.player )
        pygame.display.update()
    #================================================================
    def draw(self):
        self.background.draw()
        self.player.draw()
        self.npcs.draw()
        self.sprites.draw(self.janela)
        self.sight.draw()    
    #================================================================ 
    def menu_loop(self):
        self.background.update(6)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()  
                if(keys[pygame.K_RETURN]):
                    self.game_paused = False
                    
        self.background.draw()
    #================================================================
    def draw_text(self, txt: str, pos = (0, 0), color = [0,0,0], font: str = "Arial", font_size: int = 40):
        self.janela.blit(create_text(txt, font, font_size, color), pos)
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