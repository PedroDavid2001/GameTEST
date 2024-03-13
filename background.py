import pygame
from utils import *

# Paths das imagens dos cenarios
scn_1 = 'assets/bg1.png'
scn_2 = 'assets/bg2.png'
scn_3 = 'assets/bg3.png'
scn_4 = 'assets/bg4.png'
scn_5 = 'assets/bg5.png'
scn_6 = 'assets/bg6.png'

class BackGround(pygame.sprite.Sprite):
    def __init__(self, janela):
        pygame.sprite.Sprite.__init__(self) 
        
        self.bg = []
        self.bg.append( self.load_img(scn_1) )
        self.bg.append( self.load_img(scn_2) )
        self.bg.append( self.load_img(scn_3) )
        self.bg.append( self.load_img(scn_4) )
        self.bg.append( self.load_img(scn_5) )
        self.bg.append( self.load_img(scn_6) )
        
        self.image = self.bg[0]
        self.screen = janela
        self.rect = self.image.get_rect()
        self.rect.topleft = 0, 0
    #================================================================
    def load_img(self, path : str):
        return pygame.transform.scale( pygame.image.load(path), (screen_width, screen_height) )
    #================================================================
    def update(self, current_scenario : int):
        self.image = self.bg[ current_scenario ]
    #================================================================
    def draw(self):
        self.screen.blit(self.image, self.rect, None)
    #================================================================