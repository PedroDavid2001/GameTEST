import pygame

#INTERACTIONS TABLE
# 1 - LOOK
# 2 - TAKE
# 3 - PUNCH / SLAP
# 4 - AIM (WITH WEAPON)
# 5 - TALK

class NPC(pygame.sprite.Sprite):
    def __init__(self, body, face, janela):
        pygame.sprite.Sprite.__init__(self)
        self.body = pygame.image.load(body)    # body sprites path
        self.face = pygame.image.load(face)    # face sprites path
        self.curr = 0
        self.screen = janela
        self.rect = self.body.get_rect()
        self.rect.topleft = 100, 100
        
    def update(self, x, y):
        self.rect.topleft = x, y
        return
    
    def draw(self):
        self.screen.blit( self.body, self.rect, None )
        self.screen.blit( self.face, self.rect, None )