MCBed = "assets/mc_bed.png"
Drawer = "assets/drawer.png"
Bart = [ "assets/Bart_Simpson.png" ]

# listas de itens [nome, x, y]
MCBEDROOM_ITENS = [
    [MCBed, 325, 450, "Deitar-se"],
    [Drawer, 780, 350, "Abrir"]
]

# backgrounds
MCBEDROOM_BACKGROUND = "assets/mc_bedroom.png"
MAINMENU_BACKGROUND = "assets/menu_bg.png"

# listas de npcs
MCBEDROOM_NPCS = [
    [Bart, 300, 350, "a a a a a a a a a s s s s s s s s s d d d d d d d d d w w w w w w w w w"],
]

# levels [background, npcs, itens]
MCBEDROOM = [MCBEDROOM_BACKGROUND, MCBEDROOM_NPCS, MCBEDROOM_ITENS]
MAINMENU = [MAINMENU_BACKGROUND, None, None]