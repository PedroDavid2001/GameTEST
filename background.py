import pygame
from utils import *

class BackGround(pygame.sprite.Sprite):
    def __init__(self, janela : pygame.Surface, img_path : str, floor_path : str):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.transform.scale( pygame.image.load(img_path), (screen_width, screen_height) )
        self.floor = pygame.transform.scale( pygame.image.load(floor_path), (screen_width, screen_height / 3) )
        self.screen = janela
        self.floor_rect = self.floor.get_rect()
        self.floor_rect.center = [screen_width/2, screen_height*0.833]
    #================================================================
    def update(self):
        return
    #================================================================
    def get_rect(self):
        return self.floor_rect
    #================================================================
    def bg_draw(self):
        self.screen.blit(self.image, (0,0), None)
        self.screen.blit(self.floor, self.floor_rect, None)
    #================================================================