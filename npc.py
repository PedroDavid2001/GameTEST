import pygame

#INTERACTIONS TABLE
# 1 - LOOK
# 2 - TAKE
# 3 - PUNCH / SLAP
# 4 - AIM (WITH WEAPON)
# 5 - TALK

class NPC(pygame.sprite.Sprite):
    def __init__(self, img_paths, janela, move_set = ''):
        pygame.sprite.Sprite.__init__(self)
        self.screen = janela
        # Array de imagens do npc
        self.images = []
        # Array de booleans que definem se a imagem neste indice deve ser exibida
        self.display_img = []
        # Array com retangulos individuais para cada imagem
        self.rects = []
        # Array de strings que determinam a movimentacao
        self.movements = move_set.split()
        # Indice que determina o proximo movimento do npc
        self.curr_mvmt = 0
        # Contador para controlar movimento
        self.move_ctrl = 0
        # Configura imagens
        for i, path in enumerate(img_paths):
            self.display_img.append(False)
            self.images.append(pygame.image.load(path))
            self.rects.append(self.images[i].get_rect())
            self.rects[i].center = 100, 100
        
    def update(self, x, y, curr_imgs):
        # Verifica colisoes
        self.collision()
        # curr_imgs armazena as posicoes das imagens que devem ser exibidas
        for value in curr_imgs:
            self.display_img[value] = True
            # escalona a lista de movimento a cada teste de update
            if(self.move_ctrl == 0):
                self.curr_mvmt = (self.curr_mvmt + 1) % len(self.movements)
                self.move(value)
                self.move_ctrl += 1
            elif(self.move_ctrl == 6):
                self.move_ctrl = 0
            else:
                self.move_ctrl += 1
                
    # Metodo que realiza movimento em um rect do npc. 
    # 'rct' se trata do indice do rect atual
    def move(self, rct):
        if(self.movements[self.curr_mvmt] == 'up'):
            self.rects[rct].move_ip(0, -5)
        elif(self.movements[self.curr_mvmt] == 'down'):
            self.rects[rct].move_ip(0, 5)
        elif(self.movements[self.curr_mvmt] == 'left'):
            self.rects[rct].move_ip(-5, 0)
        elif(self.movements[self.curr_mvmt] == 'right'):
            self.rects[rct].move_ip(5, 0)
            
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