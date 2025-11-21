import pyxel

class Camion:
    # define los atributos de la clase
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
        pass