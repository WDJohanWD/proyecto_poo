from Dado import Dado
from Queso import Queso
from Preguntas import Preguntas
from jugador import Jugador
class Tablero:
    def __init__(self, jugador) -> None:
        self.casilla = 0
        self.jugador = jugador
        self.preguntas_instancia = Preguntas()
        self.pregunta_actual = {}
        self.categoria = ''
        self.queso_instancia = Queso()

    def mover(self) -> None:
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
        if self.pregunta_actual:
            print(f'La categoría es {self.categoria}')
            print(f"\n{self.pregunta_actual['enunciado']}")
            for opcion in self.pregunta_actual['opciones']:
                print(opcion)

            respuesta_usuario = input("Tu respuesta: ").lower()
            return respuesta_usuario == self.pregunta_actual['respuesta_correcta']

        return False

    def posicion_pregunta(self) -> None:
        if self.casilla not in [7, 14, 21, 28, 35, 42]:
            posicion = self.casilla % 6
            self.preguntas_instancia.elegir_pregunta(posicion)
            self.pregunta_actual, self.categoria = self.preguntas_instancia.obtener_pregunta_actual()
        else:
            self.calcular_quesos()
            self.pregunta_actual, self.categoria = self.preguntas_instancia.obtener_pregunta_actual()

    def calcular_quesos(self) -> None:
        if self.casilla == 7:
            self.preguntas_instancia.elegir_pregunta(1)
            self.pregunta_actual, self.categoria = self.preguntas_instancia.obtener_pregunta_actual()
            if self.imprimir_posicion_pregunta():
                self.queso_instancia.conseguir_queso(self.categoria)
                print(f'Cantidad de quesos obtenidos: {self.queso_instancia.cantidad_quesos()}')
        elif self.casilla == 14:
            self.preguntas_instancia.elegir_pregunta(2)
            self.pregunta_actual, self.categoria = self.preguntas_instancia.obtener_pregunta_actual()
            if self.imprimir_posicion_pregunta():
                self.queso_instancia.conseguir_queso(self.categoria)
                print(f'Cantidad de quesos obtenidos: {self.queso_instancia.cantidad_quesos()}')
        elif self.casilla == 21:
            self.preguntas_instancia.elegir_pregunta(3)
            self.pregunta_actual, self.categoria = self.preguntas_instancia.obtener_pregunta_actual()
            if self.imprimir_posicion_pregunta():
                self.queso_instancia.conseguir_queso(self.categoria)
                print(f'Cantidad de quesos obtenidos: {self.queso_instancia.cantidad_quesos()}')
        elif self.casilla == 28:
            self.preguntas_instancia.elegir_pregunta(4)
            self.pregunta_actual, self.categoria = self.preguntas_instancia.obtener_pregunta_actual()
            if self.imprimir_posicion_pregunta():
                self.queso_instancia.conseguir_queso(self.categoria)
                print(f'Cantidad de quesos obtenidos: {self.queso_instancia.cantidad_quesos()}')
        elif self.casilla == 35:
            self.preguntas_instancia.elegir_pregunta(5)
            self.pregunta_actual, self.categoria = self.preguntas_instancia.obtener_pregunta_actual()
            if self.imprimir_posicion_pregunta():
                self.queso_instancia.conseguir_queso(self.categoria)
                print(f'Cantidad de quesos obtenidos: {self.queso_instancia.cantidad_quesos()}')
        elif self.casilla == 42:
            self.preguntas_instancia.elegir_pregunta(6)
            self.pregunta_actual, self.categoria = self.preguntas_instancia.obtener_pregunta_actual()
            if self.imprimir_posicion_pregunta():
                self.queso_instancia.conseguir_queso(self.categoria)
                print(f'Cantidad de quesos obtenidos: {self.queso_instancia.cantidad_quesos()}')

        


if __name__ == "__main__":
    # Creamos dos jugadores
    jugador1 = Jugador("Jugador 1")
    jugador2 = Jugador("Jugador 2")
    
    # Creamos un tablero para cada jugador
    tablero_jugador1 = Tablero(jugador1)
    tablero_jugador2 = Tablero(jugador2)
    
    # Iteramos hasta que uno de los jugadores gane
    while not jugador1.ha_ganado() and not jugador2.ha_ganado():
        # Turno del jugador 1
        print(f"\nTurno de {jugador1.nombre}:")
        tablero_jugador1.mover()
        tablero_jugador1.posicion_pregunta()
        while tablero_jugador1.imprimir_posicion_pregunta():
            tablero_jugador1.mover()
            tablero_jugador1.posicion_pregunta()
        
        # Si el jugador 1 ganó, salimos del bucle
        if jugador1.ha_ganado():
            print(f"\n¡{jugador1.nombre} ha ganado!")
            break
        
        # Turno del jugador 2
        print(f"\nTurno de {jugador2.nombre}:")
        tablero_jugador2.mover()
        tablero_jugador2.posicion_pregunta()
        while tablero_jugador2.imprimir_posicion_pregunta():
            tablero_jugador2.mover()
            tablero_jugador2.posicion_pregunta()
        
        # Si el jugador 2 ganó, salimos del bucle
        if jugador2.ha_ganado():
            print(f"\n¡{jugador2.nombre} ha ganado!")
            break
