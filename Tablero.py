from Dado import Dado
from Queso import Queso
from Preguntas import Preguntas

class Tablero:
    casilla: int
    dado: Dado
    preguntas_instancia: Preguntas
    pregunta_actual: dict
    categoría: str
    queso_instancia: Queso

    def __init__(self, jugador) -> None:
        #Inicializa el tablero.
        self.casilla = 0
        self.preguntas_instancia = Preguntas()
        self.pregunta_actual = {}
        self.categoría = ''
        self.queso_instancia = Queso()

    def mover(self) -> None:
        #Mueve al jugador según el resultado del dado.
        dado = Dado()
        dado_lanzado = dado.lanzar_dado()
        while True:
            movimiento = input(
                f'Estás en la casilla {self.casilla} Quieres AVANZAR o RETROCEDER: {dado_lanzado} casillas ').lower()
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

    def imprimir_posicion_pregunta(self) -> bool:
        #Imprime la pregunta y devuelve si el usuario acertó o no.
        if self.pregunta_actual:
            print(f'La categoría es {self.categoría}')
            print(f"\n{self.pregunta_actual['enunciado']}")
            for opcion in self.pregunta_actual['opciones']:
                print(opcion)

            respuesta_usuario = input("Tu respuesta: ").lower()
            return respuesta_usuario == self.pregunta_actual['respuesta_correcta']

        return False

    def posicion_pregunta(self) -> None:
        #Calcula la posición de la casilla para elegir una pregunta.
        if self.casilla != 7 and self.casilla != 14 and self.casilla != 21 and self.casilla != 28 and self.casilla != 35 and self.casilla != 42:
            posicion = self.casilla % 6
            self.preguntas_instancia.elegir_pregunta(posicion)
            self.pregunta_actual, self.categoría = self.preguntas_instancia.obtener_pregunta_actual()
        else:
            self.calcular_quesos()
            self.pregunta_actual, self.categoría = self.preguntas_instancia.obtener_pregunta_actual()

    def calcular_quesos(self) -> None:
        #Calcula la cantidad de quesos obtenidos en una casilla especial.
        if self.casilla == 7:
            self.preguntas_instancia.elegir_pregunta(1)
            self.pregunta_actual, self.categoría = self.preguntas_instancia.obtener_pregunta_actual()

            if self.imprimir_posicion_pregunta():
                self.queso_instancia.conseguir_queso(self.categoría)
                print(f'Cantidad de quesos obtenidos: {self.queso_instancia.cantidad_quesos()}')
        elif self.casilla == 14:
            self.preguntas_instancia.elegir_pregunta(2)
            self.pregunta_actual, self.categoría = self.preguntas_instancia.obtener_pregunta_actual()

            if self.imprimir_posicion_pregunta():
                self.queso_instancia.conseguir_queso(self.categoría)
                print(f'Cantidad de quesos obtenidos: {self.queso_instancia.cantidad_quesos()}')
        elif self.casilla == 21:
            self.preguntas_instancia.elegir_pregunta(3)
            self.pregunta_actual, self.categoría = self.preguntas_instancia.obtener_pregunta_actual()

            if self.imprimir_posicion_pregunta():
                self.queso_instancia.conseguir_queso(self.categoría)
                print(f'Cantidad de quesos obtenidos: {self.queso_instancia.cantidad_quesos()}')
        elif self.casilla == 28:
            self.preguntas_instancia.elegir_pregunta(4)
            self.pregunta_actual, self.categoría = self.preguntas_instancia.obtener_pregunta_actual()

            if self.imprimir_posicion_pregunta():
                self.queso_instancia.conseguir_queso(self.categoría)
                print(f'Cantidad de quesos obtenidos: {self.queso_instancia.cantidad_quesos()}')
        elif self.casilla == 35:
            self.preguntas_instancia.elegir_pregunta(5)
            self.pregunta_actual, self.categoría = self.preguntas_instancia.obtener_pregunta_actual()

            if self.imprimir_posicion_pregunta():
                self.queso_instancia.conseguir_queso(self.categoría)
                print(f'Cantidad de quesos obtenidos: {self.queso_instancia.cantidad_quesos()}')
        elif self.casilla == 42:
            self.preguntas_instancia.elegir_pregunta(6)
            self.pregunta_actual, self.categoría = self.preguntas_instancia.obtener_pregunta_actual()

            if self.imprimir_posicion_pregunta():
                self.queso_instancia.conseguir_queso(self.categoría)
                print(f'Cantidad de quesos obtenidos: {self.queso_instancia.cantidad_quesos()}')

if __name__ == '__main__':
    tablero1 = Tablero('jugador')
    tablero1.mover()
    tablero1.posicion_pregunta()
    while tablero1.imprimir_posicion_pregunta():
        tablero1.mover()
        tablero1.posicion_pregunta()