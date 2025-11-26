import pyxel
import constantes
from personajes import Personaje, Mario, Luigi
from constantes import *
from plataformas import Plataforma
from cintas import Cinta
from escenario import Escenario


class Tablero:

    def __init__(self, ancho: int, alto: int):
        '''
        :param ancho: el ancho del tablero
        :param alto: el alto del tablero
        '''
        # definimos los atributos
        self.ancho = ancho
        self.alto = alto

        # creamos una instancia del objeto Mario en las coordenadas indicadas
        self.mario = Mario(constantes.X_INICIAL_MARIO, constantes.Y_INICIAL_MARIO)

        # creamos una instancia del objeto Luigi en las coordenadas indicadas
        self.luigi = Luigi(constantes.X_INICIAL_LUIGI, constantes.Y_INICIAL_LUIGI)

        self.escenario = Escenario()

        # crea el tablero
        pyxel.init(self.ancho, self.alto, title='Mario Bross')

        # accede al recurso de pyxres donde tenemos todos los sprites
        pyxel.load('assets/assets.pyxres')

        # inicia el programa
        pyxel.run(self.update, self.draw)


    # properties y setters
    @property
    def ancho(self) -> int:
        return self._ancho

    @property
    def alto(self) -> int:
        return self._alto

    @ancho.setter
    def ancho(self, nuevo_valor):
        if type(nuevo_valor) != int:
            raise TypeError('el ancho debe de ser un entero')
        if not 0 < nuevo_valor < 500:
            raise ValueError(f'el ancho debe de estar entre 0 y 500: {nuevo_valor}')
        self._ancho = nuevo_valor

    @alto.setter
    def alto(self, nuevo_valor):
        if type(nuevo_valor) != int:
            raise TypeError('el alto debe de ser un entero')
        if not 0 < nuevo_valor < 500:
            raise ValueError(f'el alto debe de estar entre 0 y 500: {nuevo_valor}')
        self._alto = nuevo_valor


    def update(self):
        '''
        este método se llama 30 veces por segundo y es el que hace que haya cambios en nuestro programa.
        aquí añadimos lo que el programa debe de hacer en el caso de que se pulse una tecla en concreto
        y todas las llamadas a las funciones características de cada personaje.
        '''


        # para cerrar el juego:
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        '''
        este método se llama 30 veces por segundo al igual que update, la diferencia esque este método
        "dibuja" todo lo que aparece en la pantalla para que el usuario lo pueda ver el juego en funiconamiento.
        Desde aquí llamamos a todos los draw concretos de cada personaje del juego y a otros métodos importantes.
        '''
        # borra _todo lo que había antes
        pyxel.cls(0)

        self.mario.draw()
        self.luigi.draw()
        self.escenario.draw()
