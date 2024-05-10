import pygame
from utils import velocity_scalling
from player import *
from main import Game

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
        # Array de booleans que definem se a imagem neste indice deve ser exibida
        self.display_img = [bool]
        # Array com retangulos individuais para cada imagem
        self.rects = []
        # Array de strings que determinam a movimentacao
        self.movements = move_set.split()
        # Indice que determina o proximo movimento do npc
        self.curr_mvmt = 0
        # Contador para controlar movimento
        self.position = init_pos
        # Configura imagens
        for i, path in enumerate(img_paths):
            self.display_img.append(False)
            self.images.append(pygame.image.load(path))
            self.rects.append(self.images[i].get_rect())
            self.rects[i].center = init_pos
    #================================================================    
    def update(self, curr_imgs : list[int], player : Player):
        # curr_imgs armazena as posicoes das imagens que devem ser exibidas
        for value in curr_imgs:
            self.display_img[value] = True
            # escalona a lista de movimento a cada teste de update
            self.curr_mvmt = (self.curr_mvmt + 1) % len(self.movements)
            self.move(value)
        # Verifica colisoes
        self.collision(player)
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
    def collision(self, player: Player):
        # Verifica colisao com mouse
        [x, y] = pygame.mouse.get_pos() # [0] = x, [1] = y
        for i, display in enumerate(self.display_img):
            if display is True:
                if pygame.Rect.collidepoint(self.rects[i], pygame.mouse.get_pos()):
                    self.game.janela.blit( self.images[2], self.rects[2], None)
                elif pygame.Rect.colliderect(self.rects[i], player.get_rect()):
                    if(player.is_attacking() is True):
                        self.game.draw_text("damage", self.position, (255,255,255))
    #================================================================    
    def draw(self):
        # Percorre o array de booleans para encontrar quais estao settados para True
        for i, display in enumerate(self.display_img):
            if display is True:
                self.game.janela.blit( self.images[i], self.rects[i], None)
                # Reseta o valor para garantir que nao repetira no proximo update
                self.display_img[i] = False     