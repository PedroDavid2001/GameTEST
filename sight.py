import pygame

class Sight(pygame.sprite.Sprite):
    def __init__(self, janela):
        pygame.sprite.Sprite.__init__(self) 
        self.sprites = []
        self.effects = []
        self.rects = []
        self.fx_rects = []
        self.curr = 2
        
        # Imagens do cursor
        self.sprites.append( pygame.image.load('assets/punch.png') )
        self.sprites.append( pygame.image.load('assets/sight.png') )
        self.sprites.append( pygame.image.load('assets/eye.png') )
        self.sprites.append( pygame.image.load('assets/take.png') )
        
        for i, img in enumerate(self.sprites):
            self.rects.append(img.get_rect())
            self.rects[i].topleft = 0, 0

        # Imagens dos efeitos de interações do cursor
        self.effects.append( pygame.image.load('assets/punch_fx.png') )
        self.effects.append( pygame.image.load('assets/sight_fx.png') )
        
        for i, img in enumerate(self.effects):
            self.fx_rects.append(img.get_rect())
            self.fx_rects[i].topleft = 0, 0

        #Atributos adicionais
        self.screen = janela
        self.clicking = False
   
    def update(self, event):
   
        self.clicking = False

        if( event.type == pygame.MOUSEWHEEL ):
            if event.y < 0:
                if self.curr > 0:
                    self.curr -= 1
            elif self.curr < (len( self.sprites ) - 1):
                    self.curr += 1
        elif( event.type == pygame.MOUSEBUTTONDOWN ):
            self.clicking = True

        mouse_pos = pygame.mouse.get_pos()
        self.rects[self.curr].center = mouse_pos[0], mouse_pos[1]
        if(self.clicking is True and self.curr < len( self.effects )):
            self.fx_rects[self.curr].center = mouse_pos[0], mouse_pos[1]

    def draw(self):
        self.screen.blit(self.sprites[self.curr], self.rects[self.curr], None)
        
        if(self.clicking is True and self.curr < len( self.effects )):
            self.screen.blit(self.effects[self.curr], self.fx_rects[self.curr], None)
