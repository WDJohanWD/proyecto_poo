from Dado import Dado
from Queso import Queso
from Preguntas import Preguntas

class Tablero:
    CASILLAS: int = 42
    CASILLA_DEP: int = 7
    CASILLA_GEO: int = 14
    CASILLA_ART: int = 21
    CASILLA_LIT: int = 28
    CASILLA_CIE: int = 35
    CASILLA_ENT: int = 42
    LISTA_CASILLAS: list = [CASILLA_DEP, CASILLA_GEO, CASILLA_ART, CASILLA_LIT, CASILLA_CIE, CASILLA_ENT]
    
    def __init__(self, jugador: object) -> None:
        self.casilla: int = 0
        self.jugador: object = jugador
        self.preguntas_instancia: Preguntas = Preguntas()
        self.pregunta_actual: dict = {}
        self.categoria: str = ''
        self.queso_instancia: Queso = Queso()

    def mover(self) -> None:
        dado: Dado = Dado()
        dado_lanzado: int = dado.lanzar_dado()
        while True:
            movimiento: str = input(
                f'Estás en la casilla {self.casilla} Quieres AVANZAR o RETROCEDER: {dado_lanzado} casillas ').lower()
            if movimiento == 'avanzar':
                num_movimiento: int = self.casilla + dado_lanzado
                self.casilla = num_movimiento % Tablero.CASILLAS
                break
            elif movimiento == 'retroceder':
                if self.casilla - dado_lanzado < 0:
                    self.casilla = Tablero.CASILLAS - (dado_lanzado - self.casilla)
                else:
                    self.casilla -= dado_lanzado
                break
            else:
                print("Por favor, escribe 'avanzar' o 'retroceder'.")

    def imprimir_posicion_pregunta(self) -> bool:
        if self.pregunta_actual:
            print(f'\nLa categoría es {self.categoria}')
            print(f"\n{self.pregunta_actual['enunciado']}")
            for opcion in self.pregunta_actual['opciones']:
                print(opcion)

            respuesta_usuario: str = input("Tu respuesta: ").lower()
            return respuesta_usuario == self.pregunta_actual['respuesta_correcta']

        return False

    def posicion_pregunta(self) -> None:
        if self.casilla not in [Tablero.CASILLA_DEP, Tablero.CASILLA_GEO, Tablero.CASILLA_ART,
                                Tablero.CASILLA_LIT, Tablero.CASILLA_CIE, Tablero.CASILLA_ENT]:
            posicion: int = self.casilla % len(Tablero.LISTA_CASILLAS)
            self.preguntas_instancia.elegir_pregunta(posicion)
            self.pregunta_actual, self.categoria = self.preguntas_instancia.obtener_pregunta_actual()
            self.imprimir_posicion_pregunta()
        else:
            self.calcular_quesos()

    def calcular_quesos(self) -> None:
        casilla_especial: dict = {
            Tablero.CASILLA_DEP: 1,
            Tablero.CASILLA_GEO: 2,
            Tablero.CASILLA_ART: 3,
            Tablero.CASILLA_LIT: 4,
            Tablero.CASILLA_CIE: 5,
            Tablero.CASILLA_ENT: 6
        }
        if self.casilla in casilla_especial:
            self.procesar_pregunta(casilla_especial[self.casilla])

    def procesar_pregunta(self, indice: int) -> None:
        self.preguntas_instancia.elegir_pregunta(indice)
        self.pregunta_actual, self.categoria = self.preguntas_instancia.obtener_pregunta_actual()
        if self.imprimir_posicion_pregunta():
            self.queso_instancia.conseguir_queso(self.categoria)
            print(f'Cantidad de quesos obtenidos: {self.queso_instancia.cantidad_quesos()}')
