'''
usamos este archivo para guardar todas las constantes, para que en el caso de que haya que cambiar una
nos sea sencillo encontrarla.
'''

# medidas del tablero

ANCHO = 384
ALTO = 256

# niveles de dificultad


'''
creamos la tupla sprite de cada personaje individual
la estructura es (banco_imagen, coordenada x en el image bank, coordenada y en el image bank, ancho, alto, escala (opcional))
'''
# protagonistas
X_INICIAL_MARIO = 264
Y_INICIAL_MARIO = 232


# estructura: (img bank, u, v, w, h)
SPRITE_MARIO = (1, 48, 16, 16, 16)
SPRITE_MARIO_PISO_1 = (1, 48, 0, 16, 16)


X_INICIAL_LUIGI = 104
Y_INICIAL_LUIGI = 221


SPRITE_LUIGI = (1, 64, 0, 16, 16)
SPRITE_LUIGI_PISO_3 = (1, 64, 16, 16, 16)


PISO_LIMITE_MARIO = (5, 7, 9, 5)
PISO_LIMITE_LUIGI = (6, 8, 10, 6)


# paquetes
X_INICIAL_PAQUETES = 324
Y_INICIAL_PAQUETES = 238
SPRITE_PAQUETES = (
    (1, 72, 128, 8, 8),
    (1, 72, 136, 8, 8),
    (1, 72, 168, 8, 8),
    (1, 72, 144, 8, 8),
    (1, 72, 152, 8, 8),
    (1, 72, 160, 8, 8)
)

PAQUETES_MINIMOS = (1, 1, 1, 1)
PISOS_IMPARES = ((3,5), (3,5,7), (3,5,7,9), (3,5))
PISOS_PARES = ((2,4,6), (2,4,6,8), (2,4,6,8,10), (2,4,6))

# escenario
# hemos creado por cada nivel 4 escenarios distintos que se van intercalando para dar efecto de movimiento
ESCENARIO_NIVEL_1 = (

        (32 * 8,  80 * 8),
        (32 * 8,  128 * 8),
        (32 * 8,  168 * 8),
        (32 * 8,  208 * 8)
)

ESCENARIO_NIVEL_2 = (

    (88 * 8,  80 * 8),
    (88 * 8,  128 * 8),
    (88 * 8,  168 * 8),
    (88 * 8,  208 * 8)

)

ESCENARIO_NIVEL_3 = (

    (144 * 8, 80 * 8),
    (144 * 8, 128 * 8),
    (144 * 8, 168 * 8),
    (144 * 8, 208 * 8)

)

ESCENARIO_NIVEL_4 = (

        (200 * 8,  80 * 8),
        (200 * 8,  128 * 8),
        (200 * 8,  168 * 8),
        (200 * 8,  208 * 8)
)

ESCENARIO = [ESCENARIO_NIVEL_1, ESCENARIO_NIVEL_2, ESCENARIO_NIVEL_3, ESCENARIO_NIVEL_4]

COLUMNA_SPRITE = (
    (0, 32 * 8, 48 * 8, ANCHO, ALTO, 14),
    (0, 88 * 8, 48 * 8, ANCHO, ALTO, 14),
    (0, 144 * 8, 48 * 8, ANCHO, ALTO, 14),
    (0, 200 * 8, 48 * 8, ANCHO, ALTO, 14)
)

# Camion

X_INICIAL_CAMION = 50
Y_INICIAL_CAMION = 153
# el camión tiene un sprite por cada paquete recogido
SPRITE_CAMION = (
    (X_INICIAL_CAMION, Y_INICIAL_CAMION, 1, 88, 104, 32, 24),
    (X_INICIAL_CAMION, Y_INICIAL_CAMION, 1, 88, 136, 32, 24),
    (X_INICIAL_CAMION, Y_INICIAL_CAMION, 1, 88, 168, 32, 24),
    (X_INICIAL_CAMION, Y_INICIAL_CAMION, 1, 88, 200, 32, 24),
    (X_INICIAL_CAMION, Y_INICIAL_CAMION, 1, 128, 104, 32, 24),
    (X_INICIAL_CAMION, Y_INICIAL_CAMION, 1, 128, 136, 32, 24),
    (X_INICIAL_CAMION, Y_INICIAL_CAMION, 1, 128, 168, 32, 24),
    (X_INICIAL_CAMION, Y_INICIAL_CAMION - 4, 1, 128, 196, 32, 28),
    (X_INICIAL_CAMION, Y_INICIAL_CAMION - 4, 1, 168, 196, 32, 28),
)