import pygame

#INTERACTIONS TABLE
# 1 - LOOK
# 2 - TAKE
# 3 - PUNCH / SLAP
# 4 - AIM (WITH WEAPON)
# 5 - TALK

class NPC(pygame.sprite.Sprite):
    def __init__(self, img_paths, janela):
        pygame.sprite.Sprite.__init__(self)
        
        self.screen = janela
        # Array de imagens do npc
        self.images = []
        # Array de booleans que definem se a imagem neste indice deve ser exibida
        self.display_img = []
        # Array com retangulos individuais para cada imagem
        self.rects = []
        
        # Configura imagens
        for i, path in enumerate(img_paths):
            self.display_img.append(False)
            self.images.append(pygame.image.load(path))
            self.rects.append(self.images[i].get_rect())
            self.rects[i].topleft = 100, 100
        
    def update(self, x, y, curr_imgs):
        # curr_imgs armazena as posicoes das imagens que devem ser exibidas
        for value in curr_imgs:
            self.display_img[value] = True
            self.rects[value].topleft = x, y
        self.collision()
   
    def collision(self):
        # Verifica colisao com mouse
        [x, y] = pygame.mouse.get_pos() # [0] = x, [1] = y
        for i, display in enumerate(self.display_img):
            if display is True:
                if pygame.Rect.collidepoint(self.rects[i], pygame.mouse.get_pos()):
                    self.screen.blit( self.images[2], self.rects[2], None)
        
    def draw(self):
        # Percorre o array de booleans para encontrar quais estao settados para True
        for i, display in enumerate(self.display_img):
            if display is True:
                self.screen.blit( self.images[i], self.rects[i], None)
                # Reseta o valor para garantir que nao repetira no proximo update
                self.display_img[i] = False     