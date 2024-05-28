import pygame
from utils import velocity_scalling, draw_text

# Constante da velocidade de movimento
vel = 2 * velocity_scalling()

idle = ['assets/Bart_Simpson.png']
right = ['assets/Bart_Simpson_walk.png']
left = ['assets/Bart_Simpson_walk.png']
atk = ['assets/Bart_Simpson_atk.png']

class Player(pygame.sprite.Sprite):
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
        self.set_images(right, 1)
        self.set_images(left, 2)
        self.set_images(atk, 3)
        # Define a acao do personagem
        self.curr_action = 0
        # Movimentos horizontal e vertical que estao sendo 
        # realizados no momento
        self.move_x = ''
        self.move_y = ''
    #================================================================
    # Retorna o rect atual
    def get_rect(self):
        return self.rects[self.curr_action]
    #================================================================ 
    # Verifica se o player esta atacando
    def is_attacking(self):
        if(self.curr_action == 3):
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
            self.rects[index].center = [100, 480]
    #================================================================       
    def update( self ):
        self.move_y = ''
        self.move_x = ''
        #for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_w]):
            self.move_y = 'w'
        elif(keys[pygame.K_s]):
            self.move_y = 's'
        
        if(keys[pygame.K_d]):
            self.move_x = 'd'
            self.curr_action = 1
        elif(keys[pygame.K_a]):
            self.move_x = 'a'
            self.curr_action = 2
        
        elif(keys[pygame.K_SPACE]):
            self.curr_action = 3
        else:
            self.curr_action = 0
        self.move()   
    #================================================================            
    # Metodo que realiza movimento em um rect do player. Tambem 
    # utilizado para verificar a posicao do player e verificar para 
    # quais lados ele pode se mover.
    def move(self):
        # Movimentos verticais
        if(self.move_y == 'w'):
            for x in range(0, self.img_qnt):
                self.rects[x].move_ip(0, -vel) 
        elif(self.move_y == 's'):
            for x in range(0, self.img_qnt):
                self.rects[x].move_ip(0, vel)
        # Movimentos horizontais
        if(self.move_x == 'd'):  
            for x in range(0, self.img_qnt):
                self.rects[x].move_ip(vel, 0)
        elif(self.move_x == 'a'):
            for x in range(0, self.img_qnt):
                self.rects[x].move_ip(-vel, 0)
    #================================================================         
    def draw(self):
        self.screen.blit( self.images[self.curr_action], self.rects[self.curr_action], None)