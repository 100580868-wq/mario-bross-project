'''
usamos este archivo para guardar todas las constantes, para que en el caso de que haya que cambiar una
nos sea sencillo encontrarla.
'''

# medidas del tablero

ANCHO = 256
ALTO = 256

# niveles de dificultad


'''
creamos la tupla sprite de cada personaje individual
la estructura es (banco_imagen, coordenada x en el image bank, coordenada y en el image bank, ancho, alto, escala (opcional))
'''
# protagonistas
X_INICIAL_MARIO = 200
Y_INICIAL_MARIO = 229
# estructura: (img bank, u, v, w, h)
SPRITE_MARIO = (1, 48, 0, 16, 16)


X_INICIAL_LUIGI = 40
Y_INICIAL_LUIGI = 221
SPRITE_LUIGI = (1, 64, 0, 16, 16)
