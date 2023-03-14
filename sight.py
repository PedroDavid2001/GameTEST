import pygame

class Sight(pygame.sprite.Sprite):
    def __init__(self, janela):
        pygame.sprite.Sprite.__init__(self) 
        self.sprites = []
        self.curr = 0
        
        self.sprites.append( pygame.image.load('assets/eye.png') )
        self.sprites.append( pygame.image.load('assets/sight.png') )
        self.sprites.append( pygame.image.load('assets/punch.png') )
        self.sprites.append( pygame.image.load('assets/take.png') )
        
        self.image = self.sprites[0]
        self.screen = janela
        self.rect = self.image.get_rect()
        self.rect.topleft = 0, 0
        self.clicking = False
   
    def update(self, event):
   
        if( event.type == pygame.MOUSEWHEEL ):
            if event.y < 0:
                if self.curr > 0:
                    self.curr -= 1
            else:
                if self.curr < (len( self.sprites ) - 1):
                    self.curr += 1

        self.image = self.sprites[ self.curr ]
        mouse_pos = pygame.mouse.get_pos()
        self.rect.center = mouse_pos[0], mouse_pos[1]

    def draw(self):
        self.screen.blit(self.image, self.rect, None)