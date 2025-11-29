import  pyxel
from personajes import Personaje
import constantes

class Paquete(Personaje):

    def __init__(self, x, y):
        # llamamos al constructor de la clase padre para pasarle los atributos que hereda de ella
        super().__init__(x, y)

        self.sprite = constantes.SPRITE_PAQUETES
        self.numero_paquetes_minimos = 1
        self.paquetes_en_juego = 0
        self.piso_actual = 1
        self.estado = 'moviendose'
        self.paquetes_listos = 0

    def update(self):
        pass

    def draw(self):

        pyxel.blt(self.x, self.y, *self.sprite, 14)

    def mover_x(self, tablero):
        if self.estado == 'moviendose':

            if self.piso_actual == 1:
                self.x -= 1

            if self.piso_actual in constantes.PISOS_PARES[tablero.nivel_dificultad]:
                self.x -= 1

            if self.piso_actual in constantes.PISOS_IMPARES[tablero.nivel_dificultad]:
                self.x += 1

    def mover_y(self, mario, luigi):

        if self.y == constantes.Y_INICIAL_PAQUETES and self.x == 274:
            if mario.piso_actual == self.piso_actual and self.piso_actual == 1:
                self.y -= 5
                self.piso_actual += 1

        if self.x > 254:
            if mario.piso_actual == self.piso_actual and self.piso_actual != 1:
                self.y -= 16
                self.piso_actual += 1

        if self.x < 114:
            if luigi.piso_actual == self.piso_actual:
                self.y -= 16
                self.piso_actual +=1



