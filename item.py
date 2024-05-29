import pygame
from utils import velocity_scalling
from main import Game
from utils import draw_text

class Item():
    def __init__(self, img_path : str, game: Game, init_pos = (100, 100), text = ''):  
        pygame.sprite.Sprite.__init__(self)
        # Configura um objeto do tipo Game com os dados do jogo principal
        self.game = game
        # Configuracao da imagem e colisao
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
        self.rect.center = init_pos
        # Movimento atual do item
        self.curr_mvmt = 0
        # texto que sera exibido quando detecta colisao
        self.text = text
    #================================================================
    def update(self):
        # Verifica colisoes
        self.collision()
    #================================================================        
    def collision(self):
        # Verifica colisao com mouse
        [x, y] = pygame.mouse.get_pos() # [0] = x, [1] = y
        if pygame.Rect.collidepoint(self.rect, pygame.mouse.get_pos()):
            draw_text(self.text, self.rect.topright, (255,255,255), 30)
    #================================================================    
    def draw(self):
        self.game.janela.blit(self.image, self.rect, None)    