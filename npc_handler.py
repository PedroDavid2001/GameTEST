import pygame
from npc import *

class NPC_Handler(pygame.sprite.Sprite):
    def __init__(self, janela):
        pygame.sprite.Sprite.__init__(self) 
            
        self.npcs = []
        paths = [ 'assets/Bart_Simpson.png', 'assets/Marge_Simpson.png', 'assets/Homer_Simpson.png' ]
        self.npcs.append([
                            NPC(paths, janela, 'up right right right right right right right right right down left left left left left left left left left'),
                        ])
        self.npcs.append([
                            NPC(paths, janela, 'up right down left'),
                        ])
        self.npcs.append([
                            NPC(paths, janela, 'up right down left'),
                        ])
        self.curr_scen = 0
        
        
    def update(self, current_scenario):
        
        if current_scenario == 0:
            self.curr_scen = current_scenario
            x = 100
            y = 100
            for npc in self.npcs[ 0 ]:
                npc.update(x, y, [ 0 ])
                x += 200
        elif current_scenario == 1:
            self.curr_scen = current_scenario
            for npc in self.npcs[ 1 ]:
                npc.update(100, 100, [ 1 ])
        elif current_scenario == 2:
            self.curr_scen = current_scenario
            for npc in self.npcs[ 2 ]:
                npc.update(100, 100, [ 2 ])

    def draw(self):
        for npc in self.npcs[ self.curr_scen ]:
            npc.draw()