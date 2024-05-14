import pygame
from utils import velocity_scalling, draw_text
from player import *

# Constante da velocidade de movimento
vel = 0.85 * velocity_scalling()

idle = ['assets/Bart_Simpson.png']
up = ['assets/Bart_Simpson_walk.png']
down = ['assets/Bart_Simpson_walk.png']
right = ['assets/Bart_Simpson_walk.png']
left = ['assets/Bart_Simpson_walk.png']
atk = ['assets/Bart_Simpson_atk.png']

class Enemy(pygame.sprite.Sprite):
    def __init__(self, janela : pygame.Surface):
        pygame.sprite.Sprite.__init__(self)
        self.screen = janela
        # Array de imagens do player
        self.images = []
        # Array com retangulos individuais para cada imagem
        self.rects = []
        # Variavel que armazena a quantidade de img sets
        self.img_qnt = 0
        # Configura imagens 
        self.set_images(idle, 0)
        self.set_images(up, 1)
        self.set_images(down, 2)
        self.set_images(right, 3)
        self.set_images(left, 4)
        self.set_images(atk, 5)
        # Define o movimento do personagem
        self.curr_mvmt = 0
        self.hp = 100
    #================================================================
    # Retorna o rect atual
    def get_rect(self):
        return self.rects[self.curr_mvmt]
    #================================================================ 
    # Verifica se o player esta atacando
    def is_attacking(self):
        if(self.curr_mvmt == 3):
            return True
        else:
            return False
    #================================================================  
    def set_images(self, paths : list[str], index : int):
        # Incrementa o contador de img sets
        self.img_qnt += 1
        for path in paths:
            self.images.append(pygame.image.load(path))
            self.rects.append(self.images[index].get_rect())
            self.rects[index].center = [900, 480]
    #================================================================        
    def collision(self, player: Player):
        if pygame.Rect.colliderect(self.rects[self.curr_mvmt], player.get_rect()):
            if(player.is_attacking() is True):
                draw_text("damage", self.rects[self.curr_mvmt].topright, (255,255,255))
                self.hp -= 10
    #================================================================       
    def update( self, floor : pygame.Rect, player : Player ):
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_w]):
            self.curr_mvmt = 1
        elif(keys[pygame.K_s]):
            self.curr_mvmt = 2
        elif(keys[pygame.K_d]):
            self.curr_mvmt = 3
        elif(keys[pygame.K_a]):
            self.curr_mvmt = 4
        elif(keys[pygame.K_SPACE]):
            self.curr_mvmt = 5
        else:
            self.curr_mvmt = 0
        self.collision(player)
        (plr_x, plr_y) = player.get_rect().center
        self.move(floor, plr_x, plr_y)   
    #================================================================            
    # Metodo que realiza movimento em um rect do player. Tambem 
    # utilizado para verificar a posicao do player e verificar para 
    # quais lados ele pode se mover.
    def move(self, floor : pygame.Rect, plr_x : int, plr_y : int ):
        
        (this_x, this_y) = self.rects[self.curr_mvmt].center
        move_x : str = ''
        move_y : str = ''
        
        if(this_x - plr_x > 10):
            move_x = 'a' 
        elif(this_x - plr_x < -10):
            move_x = 'd'
        if(this_y - plr_y > 10):
            move_y = 'w' 
        elif(this_y - plr_y < -10):
            move_y = 's' 
        
        # Movimentos verticais
        if(move_y == 'w'):
            # Se a distancia entre a base do inimigo e o topo do piso 
            # for menor que 10, o player nao podera subir
            if(self.get_rect().bottom - floor.top >= 10):
                for x in range(0, self.img_qnt):
                    self.rects[x].move_ip(0, -vel) 
        elif(move_y == 's'):
            for x in range(0, self.img_qnt):
                self.rects[x].move_ip(0, vel)
        # Movimentos horizontais
        if(move_x == 'd'):  
            for x in range(0, self.img_qnt):
                self.rects[x].move_ip(vel, 0)
        elif(move_x == 'a'):
            for x in range(0, self.img_qnt):
                self.rects[x].move_ip(-vel, 0)
    #================================================================         
    def draw(self):
        self.screen.blit( self.images[self.curr_mvmt], self.rects[self.curr_mvmt], None)
        draw_text("hp: "+str(self.hp), self.rects[self.curr_mvmt].midright, (255,190,0))