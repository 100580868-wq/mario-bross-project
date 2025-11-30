import pyxel

import constantes
from personajes import Personaje

class Camion(Personaje):

    def __init__(self, x, y):
        # llamamos al init de la clase padre para que pase por los setters
        super().__init__(x, y)

        self.estado = 'operativo'

    def update(self):
        pass

    def draw(self, tablero):

        pyxel.blt(self.x, self.y - 4, *constantes.SPRITE_CAMION[tablero.paquetes_listos], 14)

    def reparto(self, tablero):
        if self.estado == 'en reparto':
            if self.x !=  - 50:
                self.x -= 1

        if self.estado == 'volviendo':
            tablero.paquetes_listos = 0
            if self.x != constantes.X_INICIAL_CAMION:
                self.x += 1
            else:
                self.estado = 'operativo'
                tablero.contador_reparto = 0
                tablero.puntuacion += 10
                tablero.repartos_realizados += 1
                for paquete in tablero.lista_paquetes:
                    paquete.estado = 'moviendose'