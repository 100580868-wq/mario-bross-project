import pyxel
from personajes import Personaje

class Jefe(Personaje):

    def __init__(self, x, y):
        # llamamos al init de la clase padre para que pase por los setters
        super().__init__(x, y)

    def reganar(self):
        pass