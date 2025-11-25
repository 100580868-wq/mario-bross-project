'''
usamos este archivo para guardar todas las constantes, para que en el caso de que haya que cambiar una
nos sea sencillo encontrarla.
'''

# medidas del tablero

ANCHO = 1050
ALTO = 650

# niveles de dificultad


'''
creamos la tupla sprite de cada personaje individual
la estructura es (banco_imagen, coordenada x en el image bank, coordenada y en el image bank, ancho, alto, escala (opcional))
'''
# protagonistas
X_INICIAL_MARIO = ANCHO - 200 - 12
Y_INICIAL_MARIO = 550
SPRITE_MARIO = (0, 8, 1, 16, 16)


X_INICIAL_LUIGI = 300
Y_INICIAL_LUIGI = 550
SPRITE_LUIGI = (1, 2, 1, 16, 16)


# plataformas
SPRITE_PLATAFORMA_1 = (2, 64, 52, 16, 3)
SPRITE_PLATAFORMA_2 = (2, 16, 39, 32, 1)
SPRITE_PLATAFORMA_3 = (2, 64, 29, 40, 1)

SPRITES_PLATAFORMAS = {
    'PLATAFORMA_1': SPRITE_PLATAFORMA_1,
    'PLATAFORMA_2': SPRITE_PLATAFORMA_2,
    'PLATAFORMA 3': SPRITE_PLATAFORMA_3
}


LISTA_PLATAFORMAS = (
    (830, 588, 'PLATAFORMA_1'),

)
