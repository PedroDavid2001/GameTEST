import pygame

idle = ['assets/Bart_Simpson.png', 'assets/Marge_Simpson.png', 'assets/Homer_Simpson.png']
up = ['assets/Bart_Simpson.png', 'assets/Marge_Simpson.png', 'assets/Homer_Simpson.png']
down = ['assets/Bart_Simpson.png', 'assets/Marge_Simpson.png', 'assets/Homer_Simpson.png']
right = ['assets/Bart_Simpson.png', 'assets/Marge_Simpson.png', 'assets/Homer_Simpson.png']
left = ['assets/Bart_Simpson.png', 'assets/Marge_Simpson.png', 'assets/Homer_Simpson.png']

class Player(pygame.sprite.Sprite):
    def __init__(self, janela):
        pygame.sprite.Sprite.__init__(self)
        self.screen = janela
        # Array de imagens do player
        self.images = [ [],[],[],[],[] ]
        # Array com retangulos individuais para cada imagem
        self.rects = [ [],[],[],[],[] ]
        # Configura imagens 
        self.set_images(idle, 0)
        self.set_images(up, 1)
        self.set_images(down, 2)
        self.set_images(right, 3)
        self.set_images(left, 4)
        # Define o movimento do personagem
        self.curr_mvmt = 0
        # Define a imagem a ser exibida
        self.curr_img = 0  
          
    def set_images(self, paths, index):
        for i, path in enumerate(paths):
            self.images[index].append(pygame.image.load(path))
            self.rects[index].append(self.images[i].get_rect())
            self.rects[index][i].center = [100, 100]
            
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if(keys[pygame.K_UP]):
                    self.curr_mvmt = 1
                    self.curr_img = 0
                elif(keys[pygame.K_DOWN]):
                    self.curr_mvmt = 2
                    self.curr_img = 0
                elif(keys[pygame.K_RIGHT]):
                    self.curr_mvmt = 3
                    self.curr_img = 0
                elif(keys[pygame.K_LEFT]):
                    self.curr_mvmt = 4
                    self.curr_img = 0
            else:
                self.curr_mvmt = 0
                self.curr_img = 0
            
    def draw(self):
        self.screen.blit( self.images[self.curr_mvmt][self.curr_img], self.rects[self.curr_mvmt][self.curr_img], None)
        self.curr_img = (self.curr_img + 1) % len(self.images[self.curr_mvmt])