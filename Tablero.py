from Dado import Dado
from Queso import Queso
from Preguntas import Preguntas


class Tablero:
    casilla: int
    dado: Dado
    preguntas_instancia: Preguntas

    # MÉTODO CONSTRUCTOR
    def __init__(self, casilla=0) -> None:
        self.casilla = casilla
        self.preguntas_instancia = Preguntas()
        self.pregunta_actual = ''
        self.categoría = ''

    # MÉTODO QUE UTILIZA EL DADO PARA SABER HACIA DONDE MOVERSE SI HACIA ADELANTE O ATRÁS
    def mover(self, Dado=Dado()):
        dado = Dado
        dado_lanzado = dado.lanzar_dado()
        while True:
            movimiento = input(
                f'Estás en la casilla { self.casilla} Quieres AVANZAR o RETROCEDER: {dado_lanzado} casillas ').lower()
            num_movimiento = 0
            if movimiento == 'avanzar':
                num_movimiento = self.casilla + dado_lanzado
                self.casilla = num_movimiento % 42
                break
            elif movimiento == 'retroceder':
                if self.casilla - dado_lanzado < 0:
                    self.casilla = 42 - (dado_lanzado - self.casilla)
                else:
                    self.casilla = self.casilla - dado_lanzado
                break
            else:
                print("Escribe bien las instrucciones")

<<<<<<< HEAD
    # CALCULA LA POSICIÓN DE LA CASILLA PARA ASÍ ELEGIR UNA PREGUNTA
    def posicion_pregunta(self):
        if self.casilla not in [7, 14, 21, 28, 35, 42]:
            posicion = (self.casilla - 1) % 6
            self.preguntas_instancia.elegir_pregunta(posicion)
            self.pregunta_actual, self.categoria = self.preguntas_instancia.obtener_pregunta_actual()

        else:
            if self.casilla == 7:
                self.preguntas_instancia.elegir_pregunta(1)
                if self.imprimir_posicion_pregunta():
                    print(
                        f'Ganaste Queso de la categoría {self.preguntas_instancia.categoria_actual}')

            elif self.casilla == 14:
                self.preguntas_instancia.elegir_pregunta(2)
                if self.imprimir_posicion_pregunta():
                    print(
                        f'Ganaste Queso de la categoría {self.preguntas_instancia.categoria_actual}')

            elif self.casilla == 21:
                self.preguntas_instancia.elegir_pregunta(1)
                if self.imprimir_posicion_pregunta():
                    print(
                        f'Ganaste Queso de la categoría {self.preguntas_instancia.categoria_actual}')
            elif self.casilla == 35:
                self.preguntas_instancia.elegir_pregunta(1)
                if self.imprimir_posicion_pregunta():
                    print(
                        f'Ganaste Queso de la categoría {self.preguntas_instancia.categoria_actual}')
=======
>>>>>>> nueva
    # IMPRIME LA PREGUNTA Y DEVUELVE SI ACIERTA O NO
    def imprimir_posicion_pregunta(self):
        if self.pregunta_actual:
            print(f'La categoría es {self.categoría}')
            print(f"\n{self.pregunta_actual[0]['enunciado']}")
            for opcion in self.pregunta_actual[0]['opciones']:
                print(opcion)

            respuesta_usuario = input("Tu respuesta: ").lower()

            return respuesta_usuario == self.pregunta_actual[0]['respuesta_correcta']

        return False

    # CALCULA LA POSICIÓN DE LA CASILLA PARA ASÍ ELEGIR UNA PREGUNTA
    def posicion_pregunta(self):
        if self.casilla != 7 and self.casilla != 14 and self.casilla != 21 and self.casilla != 28 and self.casilla != 35 and self.casilla != 42:
            posicion = self.casilla % 6

            self.preguntas_instancia.elegir_pregunta(posicion)
            self.pregunta_actual, self.categoría = self.preguntas_instancia.obtener_pregunta_actual()
        else:
            Tablero.calcular_quesos(self)

    def calcular_quesos(self):
        if self.casilla == 7:
            self.preguntas_instancia.elegir_pregunta(1)
            if Tablero.imprimir_posicion_pregunta(self):
                print(
                    f'Ganaste Queso de la categoría {self.categoría}')

        elif self.casilla == 14:
            self.preguntas_instancia.elegir_pregunta(2)
            if Tablero.imprimir_posicion_pregunta(self):
                print(
                    f'Ganaste Queso de la categoría {self.categoría}')

        elif self.casilla == 21:
            self.preguntas_instancia.elegir_pregunta(3)
            if Tablero.imprimir_posicion_pregunta(self):
                print(
                    f'Ganaste Queso de la categoría {self.categoría}')
        elif self.casilla == 28:
            self.preguntas_instancia.elegir_pregunta(4)
            if Tablero.imprimir_posicion_pregunta(self):
                print(
                    f'Ganaste Queso de la categoría {self.categoría}')

        elif self.casilla == 35:
            self.preguntas_instancia.elegir_pregunta(5)
            if Tablero.imprimir_posicion_pregunta(self):
                print(
                    f'Ganaste Queso de la categoría {self.categoría}')
        elif self.casilla == 42:
            self.preguntas_instancia.elegir_pregunta(6)
            if Tablero.imprimir_posicion_pregunta(self):
                print(
                    f'Ganaste Queso de la categoría {self.categoría}')


if __name__ == '__main__':
    tablero1 = Tablero()
    tablero1.mover()
    tablero1.posicion_pregunta()
    while tablero1.imprimir_posicion_pregunta():
        tablero1.mover()
        tablero1.posicion_pregunta()
