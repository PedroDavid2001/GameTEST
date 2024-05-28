import pygame
from utils import velocity_scalling
from main import Game
from utils import draw_text

class NPC(pygame.sprite.Sprite):
    def __init__(self, img_paths : list[str], game: Game, init_pos = (100, 100), move_set = ''):
        pygame.sprite.Sprite.__init__(self)
        # Configura um objeto do tipo Game com os dados do jogo principal
        self.game = game
        # Pontos de vida do npc
        self.hp = 3
        # Velocidade de movimento
        self.vel = 1.25 * velocity_scalling()
        # Array de imagens do npc
        self.images = []
        # Array com retangulos individuais para cada imagem
        self.rects = []
        # Array de strings que determinam a movimentacao
        self.movements = move_set.split()
        # Indice que determina o proximo movimento do npc
        self.curr_mvmt = 0
        # Indice que determina a imagem a ser desenhada
        self.curr_img = 0
        # Contador para controlar movimento
        self.position = init_pos
        # Configura imagens
        for i, path in enumerate(img_paths):
            self.images.append(pygame.image.load(path))
            self.rects.append(self.images[i].get_rect())
            self.rects[i].center = init_pos
    #================================================================    
    def update(self):
        # Verifica colisoes
        self.collision()
        # escalona a lista de movimento a cada teste de update
        self.curr_mvmt = (self.curr_mvmt + 1) % len(self.movements)
        self.move(self.curr_img)
    #================================================================            
    # Metodo que realiza movimento em um rect do npc. 
    # 'rct' se trata do indice do rect atual
    def move(self, rct : int):
        if(self.movements[self.curr_mvmt] == 'w'):
            self.rects[rct].move_ip(0, -self.vel)
        elif(self.movements[self.curr_mvmt] == 's'):
            self.rects[rct].move_ip(0, self.vel)
        elif(self.movements[self.curr_mvmt] == 'a'):
            self.rects[rct].move_ip(-self.vel, 0)
        elif(self.movements[self.curr_mvmt] == 'd'):
            self.rects[rct].move_ip(self.vel, 0)
        self.position = self.rects[rct].topright
    #================================================================        
    def collision(self):
        # Verifica colisao com mouse
        [x, y] = pygame.mouse.get_pos() # [0] = x, [1] = y
        if pygame.Rect.collidepoint(self.rects[self.curr_img], pygame.mouse.get_pos()):
            draw_text("mouse colidindo", self.position, (255,255,255))
    #================================================================    
    def draw(self):
        self.game.janela.blit(self.images[self.curr_img], self.rects[self.curr_img], None)    