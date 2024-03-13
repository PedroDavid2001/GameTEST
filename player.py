import pygame
from utils import *

# Constante da velocidade de movimento
vel = 3 * velocity_scalling()

idle = ['assets/Bart_Simpson.png']
up = ['assets/Bart_Simpson.png']
down = ['assets/Bart_Simpson.png']
right = ['assets/Bart_Simpson.png']
left = ['assets/Bart_Simpson.png']
atk = ['assets/Bart_Simpson_atk.png']

class Player(pygame.sprite.Sprite):
    def __init__(self, janela):
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
    #================================================================
    # Retorna o rect atual
    def get_rect(self):
        return self.rects[self.curr_mvmt]
    #================================================================ 
    # Verifica se o player esta atacando
    def is_attacking(self):
        if(self.curr_mvmt == 5):
            return True
        else:
            return False
    #================================================================  
    def set_images(self, paths, index):
        # Incrementa o contador de img sets
        self.img_qnt += 1
        for path in paths:
            self.images.append(pygame.image.load(path))
            self.rects.append(self.images[index].get_rect())
            self.rects[index].center = [100, 100]
    #================================================================       
    def update(self):
        #for event in pygame.event.get():
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
        self.move()
    #================================================================            
    # Metodo que realiza movimento em um rect do player. 
    # 'rct' se trata do indice do rect atual
    def move(self):
        if(self.curr_mvmt == 1):
            for x in range(0, self.img_qnt):
                self.rects[x].move_ip(0, -vel)
        elif(self.curr_mvmt == 2):
            for x in range(0, self.img_qnt):
                self.rects[x].move_ip(0, vel)
        elif(self.curr_mvmt == 3):  
            for x in range(0, self.img_qnt):
                self.rects[x].move_ip(vel, 0)
        elif(self.curr_mvmt == 4):
            for x in range(0, self.img_qnt):
                self.rects[x].move_ip(-vel, 0)
    #================================================================         
    def draw(self):
        self.screen.blit( self.images[self.curr_mvmt], self.rects[self.curr_mvmt], None)