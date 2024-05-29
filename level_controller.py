# Contem objetos de cena
# contem NPCs
# contem um background

import pygame
from utils import screen_width, screen_height
from npc import NPC
from item import Item
from main import Game

class Level(pygame.sprite.Sprite):
    #================================================================
    # level [background, npcs, itens]
    def __init__(self, game: Game, level : list):
        pygame.sprite.Sprite.__init__(self) 
        # imagem do baackground
        self.bg : pygame.Surface
        self.load_bg(level[0])
        # instancia do game
        self.game = game
        # lista de npcs na cena
        self.lista_npc = []
        self.load_npcs(level[1])
        # lista de itens na cena
        self.lista_item = []
        self.load_itens(level[2])
    #================================================================
    def load_bg(self, path : str):
        self.bg = pygame.transform.scale( pygame.image.load(path), (screen_width, screen_height) )
    #================================================================
    def load_npcs(self, lista_npcs : list | None):
        if lista_npcs is None:
            return
        for npc in lista_npcs:
            self.lista_npc.append( NPC(npc[0], self.game, (npc[1],npc[2]), npc[3]) )
    #================================================================
    def load_itens(self, lista_itens : list | None):
        if lista_itens is None:
            return
        for item in lista_itens:
            self.lista_item.append( Item(item[0], self.game,(item[1],item[2]),item[3]) )
    #================================================================
    def update(self):
        for npc in self.lista_npc:
            npc.update()
        for item in self.lista_item:
            item.update()
    #================================================================
    def draw(self):
        self.game.janela.blit(self.bg, (0,0), None)
        for item in self.lista_item:
            item.draw()
        for npc in self.lista_npc:
            npc.draw()
        
    #================================================================