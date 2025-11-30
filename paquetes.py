import  pyxel
from personajes import Personaje
import constantes

class Paquete(Personaje):

    def __init__(self, x, y):
        # llamamos al constructor de la clase padre para pasarle los atributos que hereda de ella
        super().__init__(x, y)

        self.piso_actual = 1
        self.estado = 'moviendose'
        self.modificaciones = 0

    def update(self):
        pass

    def draw(self):

        pyxel.blt(self.x, self.y, *constantes.SPRITE_PAQUETES[self.modificaciones], 14)

    def mover_x(self, tablero):
        if self.estado == 'moviendose':

            if self.x == (384 / 2) -8 and self.modificaciones < 5:
                self.modificaciones += 1

            if self.piso_actual == 1:
                self.x -= 1

            if self.piso_actual in constantes.PISOS_PARES[tablero.nivel_dificultad]:
                self.x -= constantes.VELOCIDAD_CINTA_PAR[tablero.nivel_dificultad]

            if self.piso_actual in constantes.PISOS_IMPARES[tablero.nivel_dificultad]:
                self.x += 1

    def mover_y(self, mario, luigi, tablero):

        if self.y == constantes.Y_INICIAL_PAQUETES and self.x == 274:
            if mario.piso_actual == self.piso_actual and self.piso_actual == 1:
                self.y -= 5
                self.piso_actual += 1
                tablero.puntuacion += 1

        if self.x > 254:
            if mario.piso_actual == self.piso_actual and self.piso_actual != 1:
                self.y -= 16
                self.piso_actual += 1
                tablero.puntuacion += 1

        if self.x < 114:
            if luigi.piso_actual == self.piso_actual and not self.piso_actual == constantes.PISO_LIMITE_LUIGI[tablero.nivel_dificultad]:
                self.y -= 16
                self.piso_actual +=1
                tablero.puntuacion += 1

            if  luigi.piso_actual == self.piso_actual and self.piso_actual == constantes.PISO_LIMITE_LUIGI[tablero.nivel_dificultad]:
                tablero.paquetes_listos += 1
                tablero.puntuacion += 1
                tablero.lista_paquetes.remove(self)

