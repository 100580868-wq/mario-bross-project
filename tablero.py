import pyxel
import constantes
from personajes import Personaje, Mario, Luigi
from constantes import *
from plataformas import Plataforma
from cintas import Cinta
from escenario import Escenario
from paquetes import Paquete
from camion import Camion


class Tablero:

    def __init__(self, ancho: int, alto: int):
        '''
        :param ancho: el ancho del tablero
        :param alto: el alto del tablero
        '''
        # definimos los atributos
        self.ancho = ancho
        self.alto = alto
        self.contador_animacion = 0
        self.dificultad_seleccionada = False
        self.nivel_dificultad = 0
        self.paquete_perdido = False
        self.paquetes_listos = 0
        self.puntuacion = 0
        self.contador_reparto = 0
        self.repartos_realizados = 0
        self.paquetes_minimos = 1
        self.tiempo_creacion = 0
        self.cooldown_creacion = 15

        # creamos una instancia del objeto Mario en las coordenadas indicadas
        self.mario = Mario(constantes.X_INICIAL_MARIO, constantes.Y_INICIAL_MARIO)

        # creamos una instancia del objeto Luigi en las coordenadas indicadas
        self.luigi = Luigi(constantes.X_INICIAL_LUIGI, constantes.Y_INICIAL_LUIGI)

        # creamos una instancia de la clase Escenario
        self.escenario = Escenario()

        # creamos una instancia de la clase Camion
        self.camion = Camion(X_INICIAL_CAMION, Y_INICIAL_CAMION)

        self.lista_paquetes = []

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
        if not 0 < nuevo_valor < 5000:
            raise ValueError(f'el ancho debe de estar entre 0 y 5000: {nuevo_valor}')
        self._ancho = nuevo_valor

    @alto.setter
    def alto(self, nuevo_valor):
        if type(nuevo_valor) != int:
            raise TypeError('el alto debe de ser un entero')
        if not 0 < nuevo_valor < 5000:
            raise ValueError(f'el alto debe de estar entre 0 y 5000: {nuevo_valor}')
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

        # para elegir la dificultad:
        if not self.dificultad_seleccionada:
            if pyxel.btnp(pyxel.KEY_1):
                self.nivel_dificultad = 0
                self.dificultad_seleccionada = True
            if pyxel.btnp(pyxel.KEY_2):
                self.nivel_dificultad = 1
                self.dificultad_seleccionada = True
            if pyxel.btnp(pyxel.KEY_3):
                self.nivel_dificultad = 2
                self.dificultad_seleccionada = True
            if pyxel.btnp(pyxel.KEY_4):
                self.nivel_dificultad = 3
                self.dificultad_seleccionada = True
            return

        self.contador_animacion += 1
        if self.contador_animacion == 8:
            self.contador_animacion = 0

        # para mover a Mario
        if pyxel.btnp(pyxel.KEY_UP):
            self.mario.mover('arriba', self)

        if pyxel.btnp(pyxel.KEY_DOWN):
            self.mario.mover('abajo', self)

        # para mover a Luigi
        if pyxel.btnp(pyxel.KEY_W):
            self.luigi.mover('arriba', self)

        if pyxel.btnp(pyxel.KEY_S):
            self.luigi.mover('abajo', self)

        # calculamos los paquetes mínimos
        if self.nivel_dificultad == 0:
            # se empieza con 1, cada 50 puntos sumamos 1 extra
            extras = self.puntuacion // 50
            self.paquetes_minimos = 1 + extras

        elif self.nivel_dificultad == 1 or self.nivel_dificultad == 2:
            # se empieza con 1, cada 30 puntos sumamos 1 extra
            extras = self.puntuacion // 30
            self.paquetes_minimos = 1 + extras

        elif self.nivel_dificultad == 3:
            # se empieza con 1, cada 20 puntos sumamos 1 extra.
            extras = self.puntuacion // 20
            self.paquetes_minimos = 1 + extras

        # creación de los paquetes

        self.tiempo_creacion += 1

        # creamos un nuevo paquete si hay menos paquetes en juego que los paquetes mínimos
        if len(self.lista_paquetes) < self.paquetes_minimos:

            '''solo permitimos la creación si ha pasado el tiempo de cooldown, esto es para que si se llega a la
            puntuación necesaria para poner en juego otro paquete, a la vez que cuando se entrega un paquete al
            camión, que no se creen en el mismo instante y haya dos paquetes uno encima de otro'''

            if self.tiempo_creacion >= self.cooldown_creacion:
                self.lista_paquetes.append(Paquete(constantes.X_INICIAL_PAQUETES, constantes.Y_INICIAL_PAQUETES))
                # reiniciamos el cronómetro para dar esos instantes de diferencia entre la creación de un paquete y otro
                self.tiempo_creacion = 0

        # le damos movimiento a los paquetes
        for paquete in self.lista_paquetes:
            if paquete.estado == 'moviendose':
                paquete.mover_x(self)
                paquete.mover_y(self.mario, self.luigi, self)

        # salida del camión
        if self.paquetes_listos == 8:
            self.camion.estado = 'en reparto'
            self.camion.reparto(self)

        if self.camion.estado != 'operativo':
            for paquete in self.lista_paquetes:
                paquete.estado = 'parado'

        if self.camion.estado == 'en reparto':
            if self.contador_reparto != 300:
                self.contador_reparto += 1

        if self.contador_reparto == 300:
            self.camion.estado = 'volviendo'
            self.camion.reparto(self)


    def draw(self):
        '''
        este método se llama 30 veces por segundo al igual que update, la diferencia esque este método
        "dibuja" todo lo que aparece en la pantalla para que el usuario lo pueda ver el juego en funiconamiento.
        Desde aquí llamamos a todos los draw concretos de cada personaje del juego y a otros métodos importantes.
        '''
        # borra _todo lo que había antes
        pyxel.cls(0)

        # primero el usuario debe de elegir la dificultad, para ello mostramos el menú de dificultad:
        if not self.dificultad_seleccionada:
            pyxel.bltm(0, 0, 1, 0, 0, constantes.ANCHO, constantes.ALTO)
            pyxel.text(constantes.ANCHO // 3, 20, 'elige la dificultad', 7)
            pyxel.text(constantes.ANCHO // 3, 50, 'nivel: facil -> pulsa 1', 7)
            pyxel.text(constantes.ANCHO // 3, 70, 'nivel: medio -> pulsa 2', 7)
            pyxel.text(constantes.ANCHO // 3, 90, 'nivel: extremo -> pulsa 3', 7)
            pyxel.text(constantes.ANCHO // 3, 110, 'nivel: crazy -> pulsa 4', 7)
            return


        self.escenario.draw(self)
        self.mario.draw(self.camion)
        self.luigi.draw(self.camion)
        self.camion.draw(self)
        for paquete in self.lista_paquetes:
            if paquete.estado != 'perdido':
                paquete.draw()
        pyxel.text(250, 5, f'puntuacion {self.puntuacion}', 7)

        # TODO
        if self.paquete_perdido:
            pass

        pyxel.bltm(0 , 0, *constantes.COLUMNA_SPRITE[self.nivel_dificultad])