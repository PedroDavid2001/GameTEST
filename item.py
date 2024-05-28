import pygame
from utils import velocity_scalling
from main import Game
from utils import draw_text

class Item():
    def __init__(self, img_path : str, game: Game, init_pos = (100, 100), move_set = ''):  
        pygame.sprite.Sprite.__init__(self)
        # Configura um objeto do tipo Game com os dados do jogo principal
        self.game = game
        # Velocidade de movimento
        self.vel = 1.25 * velocity_scalling()
        # Array de strings que determinam a movimentacao
        self.movements = move_set.split()
        # Configuracao da imagem e colisao
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
        self.rect.center = init_pos
        # Movimento atual do item
        self.curr_mvmt = 0
    #================================================================
    def update(self):
        # escalona a lista de movimento a cada teste de update
        if(len(self.movements) > 0):
            self.curr_mvmt = (self.curr_mvmt + 1) % len(self.movements)
            self.move()
        # Verifica colisoes
        self.collision()
    #================================================================            
    # Metodo que realiza o movimento do rect
    def move(self):
        if(self.movements[self.curr_mvmt] == 'w'):
            self.rect.move_ip(0, -self.vel)
        elif(self.movements[self.curr_mvmt] == 's'):
            self.rect.move_ip(0, self.vel)
        elif(self.movements[self.curr_mvmt] == 'a'):
            self.rect.move_ip(-self.vel, 0)
        elif(self.movements[self.curr_mvmt] == 'd'):
            self.rect.move_ip(self.vel, 0)
    #================================================================        
    def collision(self):
        # Verifica colisao com mouse
        [x, y] = pygame.mouse.get_pos() # [0] = x, [1] = y
        if pygame.Rect.collidepoint(self.rect, pygame.mouse.get_pos()):
            draw_text("mouse colidindo", self.rect.topright, (255,255,255))
                
    #================================================================    
    def draw(self):
        self.game.janela.blit(self.image, self.rect, None)    