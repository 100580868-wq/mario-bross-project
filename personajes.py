import pyxel

class Personaje:
    # define los atributos del personaje
    def __init__(self, x, y, img, u, v):
        self.x = x
        self.y = y
        self.ancho = 8
        self.alto = 8
        # index de la imagen del sprite en el image bank del pyxres
        self.img = img
        # coordenada x de la imagen en el image bank
        self.u = u
        # coordenada y de la imagen en el image bank
        self.v = v

    def update(self):
        pass

    def draw(self):
        # construye el personaje
        pyxel.blt(self.x, self.y, self.img, self.u, self.v, self.ancho, self.alto, scale=10)

class Mario(Personaje):
    pass

class Luigi(Personaje):
    pass
