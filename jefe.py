import pyxel
from personajes import Personaje
import constantes


class Jefe(Personaje):

    def __init__(self, x, y):
        # llamamos al init de la clase padre para que pase por los setters
        super().__init__(x, y)

    def bronca_mario(self, tablero):

        if tablero.contador_animacion_jefe <= 15:
            pyxel.blt(constantes.X_JEFE_MARIO, constantes.Y_JEFE_MARIO, *constantes.SPRITE_JEFE_MARIO_1, 14)
        elif 15 < tablero.contador_animacion_jefe <= 30:
            pyxel.blt(constantes.X_JEFE_MARIO, constantes.Y_JEFE_MARIO, *constantes.SPRITE_JEFE_MARIO_2, 14)
        else:
            tablero.contador_animacion_jefe = 0

    def bronca_luigi(self, tablero):

        if tablero.contador_animacion_jefe <= 15:
            pyxel.blt(constantes.X_JEFE_LUIGI, constantes.Y_JEFE_LUIGI, *constantes.SPRITE_JEFE_LUIGI_1, 14)
        elif 15 < tablero.contador_animacion_jefe <= 30:
            pyxel.blt(constantes.X_JEFE_LUIGI, constantes.Y_JEFE_LUIGI, *constantes.SPRITE_JEFE_LUIGI_2, 14)
        else:
            tablero.contador_animacion_jefe = 0