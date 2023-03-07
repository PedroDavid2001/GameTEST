import pygame

sprite_sheet = pygame.image.load('assets/bart.png')

class Bart(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        for i in range(0, 31, 15):
            self.sprites.append( sprite_sheet.subsurface(( i, 1 ), ( 14, 32)) ) 
         
        self.curr = 0
        self.image = self.sprites[self.curr]
        self.image = pygame.transform.scale(self.image, (14*5, 32*5))
        self.rect = self.image.get_rect()
        self.rect.topleft = 150, 350
        
    def update(self):
        if self.curr > 2.0:
            self.curr = 0
            
        self.curr += 0.1
        
        self.image = self.sprites[int(self.curr)]
        self.image = pygame.transform.scale(self.image, (14*5, 32*5))