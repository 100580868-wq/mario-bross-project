import pyxel

import constantes
from personajes import Personaje

class Camion(Personaje):

    def __init__(self, x, y):
        # llamamos al init de la clase padre para que pase por los setters
        super().__init__(x, y)

    def update(self):
        pass

    def draw(self, tablero):

        pyxel.blt(*constantes.SPRITE_CAMION[tablero.paquetes_listos], 14)