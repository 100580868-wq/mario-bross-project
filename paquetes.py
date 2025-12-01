import random

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
        self.nueva_velocidad = 1

    def update(self):
        pass

    def draw(self):

        pyxel.blt(self.x, self.y, *constantes.SPRITE_PAQUETES[self.modificaciones], 14)

    def mover_x(self, tablero):
        '''hemos tenido que cambiar esta función casi entera al añadir los niveles de dificultad, porque no siempre pasaba
        por el punto medio al ir sumandole decimales en lugar de enteros'''

        if self.estado == 'moviendose':
            # definimos la x en la que se encuentra antes de ejecutarse la función y el pto medio del mapa
            x_anterior = self.x
            punto_medio = 184

            # le damos velocidades distintas dependiendo del nivel de dificultad
            if self.piso_actual == 1:
                self.x -= 1

            if self.piso_actual in constantes.PISOS_PARES[tablero.nivel_dificultad] and tablero.nivel_dificultad == 3:
                self.x -= self.nueva_velocidad

            if self.piso_actual in constantes.PISOS_IMPARES[tablero.nivel_dificultad] and tablero.nivel_dificultad == 3:
                self.x += self.nueva_velocidad

            if self.piso_actual in constantes.PISOS_PARES[tablero.nivel_dificultad] and not tablero.nivel_dificultad == 3:
                self.x -= constantes.VELOCIDAD_CINTA_PAR[tablero.nivel_dificultad]

            if self.piso_actual in constantes.PISOS_IMPARES[tablero.nivel_dificultad] and not tablero.nivel_dificultad == 3:
                self.x += constantes.VELOCIDAD_CINTA_IMPAR[tablero.nivel_dificultad]

            # comprobamos que va de derecha a izquierda y que ha pasado por el punto medio, después le sumamos una modificacion
            if self.piso_actual == 1 or self.piso_actual in constantes.PISOS_PARES[tablero.nivel_dificultad]:
                if x_anterior > punto_medio and self.x <= punto_medio:
                    if self.modificaciones < 5:
                        self.modificaciones += 1

            # comprobamos que va de izquierda a derecha y que ha pasado por el punto medio, después le sumamos una modificacion
            if self.piso_actual in constantes.PISOS_IMPARES[tablero.nivel_dificultad]:
                if x_anterior < punto_medio and self.x >= punto_medio:
                    if self.modificaciones < 5:
                        self.modificaciones += 1


    def mover_y(self, mario, luigi, tablero):

        # si se pierden, caen en picado hasta el suelo
        if self.estado == 'perdido por mario' or self.estado == 'perdido por luigi':
            if self.y < 242:
                self.y += 2

        if self.y == constantes.Y_INICIAL_PAQUETES and self.x == 274:
            if mario.piso_actual == self.piso_actual and self.piso_actual == 1:
                self.y -= 5
                self.piso_actual += 1
                tablero.puntuacion += 1
                if tablero.nivel_dificultad == 3:
                    self.nueva_velocidad = random.randint(1, 2)
            else:
                self.estado = 'perdido por mario'


        if 264 < self.x < 268:
            if mario.piso_actual == self.piso_actual and self.piso_actual != 1:
                self.y -= 16
                self.piso_actual += 1
                tablero.puntuacion += 1
                if tablero.nivel_dificultad == 3:
                    self.nueva_velocidad = random.randint(1, 2)

        # detecta cuando el paquete se encuentra en la X de mario y mario no está en su mismo piso
        if 264 < self.x < 268 and self.piso_actual in constantes.PISOS_IMPARES[tablero.nivel_dificultad]:
            if mario.piso_actual != self.piso_actual:
                self.estado = 'perdido por mario'

        if self.x < 111:
            if luigi.piso_actual == self.piso_actual and not self.piso_actual == constantes.PISO_LIMITE_LUIGI[tablero.nivel_dificultad]:
                self.y -= 16
                self.piso_actual +=1
                tablero.puntuacion += 1
                if tablero.nivel_dificultad == 3:
                    self.nueva_velocidad = random.randint(1, 2)


            if  luigi.piso_actual == self.piso_actual and self.piso_actual == constantes.PISO_LIMITE_LUIGI[tablero.nivel_dificultad]:
                tablero.paquetes_listos += 1
                tablero.puntuacion += 1
                tablero.lista_paquetes.remove(self)

        # detecta cuando el paquete se encuentra en la X de luigi y luigi no está en su mismo piso
        if self.x < 111 and self.piso_actual in constantes.PISOS_PARES[tablero.nivel_dificultad]:
            if self.piso_actual != luigi.piso_actual:
                self.estado = 'perdido por luigi'
