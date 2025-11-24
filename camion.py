import pyxel
from personajes import Personaje

class Camion(Personaje):

    def __init__(self, x ,y):
        # llamamos al constructor de la clase padre para pasarle los atributos que hereda de ella
        super().__init__(x, y)

        # creamos la tupla sprite en cada instancia de personaje porque cada uno tiene una imágen distinta
        # la estructura es (banco_imagen, coordenada x en el image bank, coordenada y en el image bank, ancho, alto, escala (opcional))
        self.sprite = (4, 4, 4, 16, 16)

    def update(self):
        pass

    def draw(self):
        pass