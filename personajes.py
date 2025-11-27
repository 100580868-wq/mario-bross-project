import pyxel

import constantes


class Personaje:
    # definimos los atributos del personaje
    def __init__(self, x: int, y: int):
        '''
        :param x : la x inicial del personaje
        :param y : la y inicial del personaje
        '''
        self.x = x
        self.y = y


    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @x.setter
    def x(self, valor_x):
        if type(valor_x) != int:
            raise TypeError('el valor de las coordenadas deben ser enteros')
        if not 0 < valor_x < constantes.ANCHO - 8:
            raise ValueError(f'el valor de la coordenada x debe estar entre {0} y {constantes.ANCHO - 8}')
        self._x = valor_x

    @y.setter
    def y(self, valor_y):
        if type(valor_y) != int:
            raise TypeError('el valor de las coordenadas deben ser enteros')
        if not 0 < valor_y < constantes.ALTO - 8:
            raise ValueError(f'el valor de la coordenada y debe estar entre {0} y {constantes.ALTO - 8}')
        self._y = valor_y


    def update(self):
        pass


    def draw(self):
        pass


class Mario(Personaje):

    def __init__(self, x, y):
        # llamamos al constructor de la clase padre para pasarle los atributos que hereda de ella
        super().__init__(x, y)

        self.sprite = constantes.SPRITE_MARIO
        self.piso_actual = 1
    def update(self):
        pass

    def draw(self):
        if self.piso_actual == 1:
            pyxel.blt(self.x, self.y, *constantes.SPRITE_MARIO_PISO_1, 14)
        else:
            pyxel.blt(self.x, self.y, *self.sprite, 14)

    def mover(self, direccion):

        # Mario se mueve en los pisos impares
        if direccion == 'arriba' and self.piso_actual != 3:
            self.y -= 25
            self.piso_actual += 1

        if direccion == 'abajo' and self.piso_actual != 1:
            self.y += 25
            self.piso_actual -= 1

class Luigi(Personaje):

    def __init__(self, x, y):
        # llamamos al init de la clase padre para que pase por los setters
        super().__init__(x, y)

        self.sprite = constantes.SPRITE_LUIGI
        self.piso_actual = 1

    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x, self.y, *self.sprite, 14)

    def mover(self, direccion):
        # Luigi se mueve en los pisos impares
        if direccion == 'arriba' and self.piso_actual != 3:
            self.y -= 32
            self.piso_actual += 1

        if direccion == 'abajo' and self.piso_actual != 1:
            self.y += 32
            self.piso_actual -= 1
