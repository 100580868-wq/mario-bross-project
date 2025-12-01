import pyxel
import constantes
from constantes import *


class Escenario:

    def __init__(self):
        # tupla de cada tilemap: (tilemap_id, u, v, w, h)
        # en el u, v hay que multiplicar la coordenada del tile por 8, cada tile son 8 pixeles
        self.fondo = (1, 48 * 8, 88 * 8, constantes.ANCHO, constantes.ALTO)
        self.escenario = ()

    def update(self):
        pass

    def draw(self, tablero):

        # crea una lista con los 4 escenarios de cada nivel
        self.escenario = [
            (*coordenadas, constantes.ANCHO, constantes.ALTO)
            for coordenadas in constantes.ESCENARIO[tablero.nivel_dificultad]
        ]

        # esto muestra en pantalla el tilemap, la estructura es: (x, y, tilemap_id, u, v, w, h)
        pyxel.bltm(0, 0, *self.fondo)

        # cada 2 frames se muestra un escenario distinto de la lista creada al principio de la función
        if tablero.contador_animacion_fondo <= 2:
            pyxel.bltm(0, 0, 0, *self.escenario[0], 14)
        elif 2 < tablero.contador_animacion_fondo <= 4:
            pyxel.bltm(0, 0, 0, *self.escenario[1], 14)
        elif 4 < tablero.contador_animacion_fondo <= 6:
            pyxel.bltm(0, 0, 0, *self.escenario[2], 14)
        elif 6 < tablero.contador_animacion_fondo <= 8:
            pyxel.bltm(0, 0, 0, *self.escenario[3], 14)
