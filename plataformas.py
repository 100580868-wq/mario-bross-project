import pyxel
from personajes import Personaje
import constantes

class Plataforma(Personaje):

    def __init__(self, x, y, tipo: str):
        '''
        :param x : coordenada x de la plataforma
        :param y : coordenada y de la plataforma
        :param tipo : el tipo de plataforma, debe ser uno de los tres en el diccionario SPRITES_PLATAFORMAS
        '''
        # llamamos al init de la clase padre para que pase por los setters
        super().__init__(x, y)
        self.tipo = tipo


    @property
    def tipo(self) -> str:
        return self._tipo

    @tipo.setter
    def tipo(self, nuevo_tipo):
        if type(nuevo_tipo) != str:
            raise TypeError
        if nuevo_tipo not in constantes.SPRITES_PLATAFORMAS:
            raise ValueError(f'no se ha encontrado ese tipo de plataforma: {nuevo_tipo}')
        self._tipo = nuevo_tipo

    # atributo de solo lectura (no hay setter)
    @property
    def sprite(self):
        '''
        :return: la correspondiente tupla SPRITE del archivo de constantes.py según su tipo
        '''
        return constantes.SPRITES_PLATAFORMAS[self.tipo]


    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x, self.y, *self.sprite, scale = 3)
