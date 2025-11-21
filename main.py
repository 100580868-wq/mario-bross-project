import pyxel
from personajes import Mario

class Tablero:

    def __init__(self):
        # crea el tablero
        pyxel.init(950, 650, title='Mario Bross')
        # accede al recurso de pyxres donde tenemos todos los sprites
        pyxel.load('my_resource.pyxres')

        # crea el atributo mario
        self.mario = Mario(100, 100, 0, 0, 0)

        # inicia el programa
        pyxel.run(self.update, self.draw)

    def update(self):
        self.mario.update()

    def draw(self):
        # borra _todo lo que había antes
        pyxel.cls(0)
        # usamos el método_ draw de mario
        self.mario.draw()

Tablero()
