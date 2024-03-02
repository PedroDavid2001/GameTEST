import pygame
from npc import *
from pathlib import Path

npc1_mvmt = Path("assets/movesets/npc1.txt").read_text()
npc2_mvmt = Path("assets/movesets/npc1.txt").read_text()
npc3_mvmt = Path("assets/movesets/npc1.txt").read_text()

class NPC_Handler(pygame.sprite.Sprite):
    def __init__(self, janela):
        pygame.sprite.Sprite.__init__(self) 
            
        self.npcs = []
        paths = [ 'assets/Bart_Simpson.png', 'assets/Marge_Simpson.png', 'assets/Homer_Simpson.png' ]
        self.npcs.append([
                            NPC(paths, janela, [150, 250], npc1_mvmt),
                        ])
        self.npcs.append([
                            NPC(paths, janela, [100, 250], npc2_mvmt),
                        ])
        self.npcs.append([
                            NPC(paths, janela, [150, 250], npc3_mvmt),
                        ])
        self.curr_scen = 0
        
        
    def update(self, current_scenario):
        
        if current_scenario == 0:
            self.curr_scen = current_scenario
            for npc in self.npcs[ 0 ]:
                npc.update([ 0 ])
        elif current_scenario == 1:
            self.curr_scen = current_scenario
            for npc in self.npcs[ 1 ]:
                npc.update([ 1 ])
        elif current_scenario == 2:
            self.curr_scen = current_scenario
            for npc in self.npcs[ 2 ]:
                npc.update([ 2 ])

    def draw(self):
        for npc in self.npcs[ self.curr_scen ]:
            npc.draw()