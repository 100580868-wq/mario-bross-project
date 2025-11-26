import pyxel
import constantes
from constantes import *


class Escenario:

    '''está en tiles, cada tile es 16x16'''

    def __init__(self):
        self.escenario = (0, 0, 0, constantes.ANCHO, constantes.ALTO, 0)

    def update(self):
        pass

    def draw(self):
        # esto muestra en pantalla el tilemap, la estructura es: (x, y, tilemap_id, u, v, w, h)
        pyxel.bltm(0, 0, *self.escenario)