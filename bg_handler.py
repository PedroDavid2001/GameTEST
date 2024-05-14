import pygame
from background import BackGround
from utils import screen_width, screen_height

# Paths das imagens dos cenarios
paths = [ 'assets/menu_bg.png',
    'assets/bg1.png',
    'assets/bg2.png',
    'assets/bg3.png',
    'assets/bg4.png',
    'assets/bg5.png',
    'assets/bg6.png' ]

# Paths das imagens dos pisos de cada cenario
floor_paths = [
    'assets/bg1_floor.png'
]

class BGHandler(pygame.sprite.Sprite):
    def __init__(self, janela : pygame.Surface):
        pygame.sprite.Sprite.__init__(self)
        self.backgrounds = []
        # Carrega as imagens de background
        for path in paths:
            self.backgrounds.append(BackGround(janela, path, floor_paths[0]))
        self.curr_bg = 0
    #================================================================
    def update(self, current_scenario : int):
        self.curr_bg = current_scenario
        self.backgrounds[self.curr_bg].update()
    #================================================================
    def get_floor_rect(self):
        return self.backgrounds[self.curr_bg].get_rect()
    #================================================================
    def draw(self):
        self.backgrounds[self.curr_bg].bg_draw()
    #================================================================