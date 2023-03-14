import pygame

class BackGround(pygame.sprite.Sprite):
    def __init__(self, janela):
        pygame.sprite.Sprite.__init__(self) 
            
        self.bg = []
        self.bg.append( pygame.image.load('assets/bg1.png') )
        self.bg.append( pygame.image.load('assets/bg2.png') )
        self.bg.append( pygame.image.load('assets/bg3.png') )
        self.bg.append( pygame.image.load('assets/bg4.png') )
        self.bg.append( pygame.image.load('assets/bg5.png') )
        self.bg.append( pygame.image.load('assets/bg6.png') )
        
        self.image = self.bg[0]
        self.screen = janela
        self.rect = self.image.get_rect()
        self.rect.topleft = 0, 0
        
    def update(self, current_scenario):
        self.image = self.bg[ current_scenario ]

    def draw(self):
        self.screen.blit(self.image, self.rect, None)