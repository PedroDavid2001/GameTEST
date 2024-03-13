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