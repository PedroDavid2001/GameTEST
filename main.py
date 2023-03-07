import pygame
from pygame.locals import *
from sys import exit
from player import *

#inicializa componentes do pygame
pygame.init()

#dimensões da tela
width = 640
height = 480

#define layout e titulo do game
janela = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game TEST')

#definindo fundo
fundo = pygame.image.load('assets/bg.png').convert()
#posição x do fundo
posX_bg = 0.0

#sprites
sprites = pygame.sprite.Group()
bart = Bart()
sprites.add(bart)

#laço principal
while True:
    #fecha o jogo se clicar no 'x'
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_RIGHT]:
            posX_bg -= 0.1
    elif tecla[pygame.K_LEFT]:
            posX_bg += 0.1
            
    janela.blit(fundo, (posX_bg, 0))
    sprites.draw(janela)
    sprites.update()
    pygame.display.update()