import pyxel

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
        if not 0 < valor_x < 500:
            raise ValueError('el valor de la coordenada x debe estar entre 0 y 500')
        self._x = valor_x

    @y.setter
    def y(self, valor_y):
        if type(valor_y) != int:
            raise TypeError('el valor de las coordenadas deben ser enteros')
        if not 0 < valor_y < 500:
            raise ValueError('el valor de la coordenada y debe estar entre 0 y 500')
        self._y = valor_y


    def update(self):
        pass


    def draw(self):
        pass


class Mario(Personaje):

    def __init__(self, x, y):
        # llamamos al constructor de la clase padre para pasarle los atributos que hereda de ella
        super().__init__(x, y)

        # creamos la tupla sprite en cada instancia de personaje porque cada uno tiene una imágen distinta
        # la estructura es (banco_imagen, coordenada x en el image bank, coordenada y en el image bank, ancho, alto, escala (opcional))
        self.sprite = (0, 0, 0, 16, 16)

    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x, self.y, *self.sprite)

    def mover(self):
        pass


class Luigi(Personaje):

    def __init__(self, x, y):
        # llamamos al init de la clase padre para que pase por los setters
        super().__init__(x, y)

        # creamos la tupla sprite en cada instancia de personaje porque cada uno tiene una imágen distinta
        # la estructura es (banco_imagen, coordenada x en el image bank, coordenada y en el image bank, ancho, alto, escala (opcional))
        self.sprite = (2, 2, 2, 16, 16)

    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x, self.y, *self.sprite)
