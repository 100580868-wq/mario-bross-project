import pyxel
from personajes import Personaje, Mario, Luigi

class Tablero:

    def __init__(self, ancho: int, alto: int):
        # definimos los atributos
        self.ancho = ancho
        self.alto = alto
        # crea el tablero
        pyxel.init(self.ancho, self.alto, title='Mario Bross')
        # accede al recurso de pyxres donde tenemos todos los sprites
        pyxel.load('my_resource.pyxres')

        # crea una instancia del objeto Mario en las coordenadas indicadas
        self.mario = Mario(100, 100)

        # inicia el programa
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        # borra _todo lo que había antes
        pyxel.cls(0)
        # usamos el método_ draw de mario
        self.mario.draw()

