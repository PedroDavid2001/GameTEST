import pygame

screen_width = 1280
screen_height = 720

# Altera a velocidade com base na resolução da tela
def velocity_scalling():
    factor_x = screen_width / 640
    factor_y = screen_height / 480
    if(factor_x > factor_y):
        return factor_x
    else:
        return factor_y
    
def create_text(txt: str, font: str, font_size: int, color):
    # Cria um objeto do tipo font do pygame
    txt_font = pygame.font.SysFont(font, font_size)
    # Renderiza o label a partir da fonte (txt_font) e da string passada (txt)
    label = txt_font.render(txt, True, color)
    return label
    