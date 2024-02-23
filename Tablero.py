from Dado import Dado
from Queso import Queso
from Preguntas import Preguntas

class Tablero:
    __casilla: int
    jugador: object
    __preguntas_instancia: Preguntas
    __pregunta_actual: dict
    __categoria: str 
    __queso_instancia: Queso 
    __respuesta_usuario:str
    CASILLAS: int = 42
    CASILLA_DEP: int = 7
    CASILLA_GEO: int = 14
    CASILLA_ART: int = 21
    CASILLA_LIT: int = 28
    CASILLA_CIE: int = 35
    CASILLA_ENT: int = 42
    LISTA_CASILLAS: list = [CASILLA_DEP, CASILLA_GEO, CASILLA_ART, CASILLA_LIT, CASILLA_CIE, CASILLA_ENT]
    
    def __init__(self, jugador: object) -> None:
        self.__casilla  = 0
        self.jugador  = jugador
        self.__preguntas_instancia = Preguntas()
        self.pregunta_actual = {}
        self.__categoria = ''
        self.queso_instancia = Queso()
        self.__respuesta_usuario=''

    def mover(self) -> None:
        dado: Dado = Dado()
        dado_lanzado: int = dado.lanzar_dado()
        while True:
            movimiento: str = input(
                f'Estás en la casilla {self.__casilla} Quieres AVANZAR o RETROCEDER: {dado_lanzado} casillas ').lower()
            if movimiento == 'avanzar':
                num_movimiento: int = self.__casilla + dado_lanzado
                self.__casilla = num_movimiento % Tablero.CASILLAS
                break
            elif movimiento == 'retroceder':
                if self.__casilla - dado_lanzado < 0:
                    self.__casilla = Tablero.CASILLAS - (dado_lanzado - self.__casilla)
                else:
                    self.__casilla -= dado_lanzado
                break
            else:
                print("Por favor, escribe 'avanzar' o 'retroceder'.")

    def imprimir_posicion_pregunta(self):
        if self.pregunta_actual:
            print(f'\nLa categoría es {self.__categoria}')
            print(f"\n{self.pregunta_actual['enunciado']}")
            for opcion in self.pregunta_actual['opciones']:
                print(opcion)

            self.__respuesta_usuario: str = input("Tu respuesta: ").lower()
            
    def verificar_respuesta(self)-> bool:
        return self.__respuesta_usuario == self.pregunta_actual['respuesta_correcta']
        
    def posicion_pregunta(self) -> None:
        if self.__casilla not in Tablero.LISTA_CASILLAS:
            posicion: int = self.__casilla % len(Tablero.LISTA_CASILLAS)
            self.__preguntas_instancia.elegir_pregunta(posicion)
            self.pregunta_actual, self.__categoria = self.__preguntas_instancia.obtener_pregunta_actual()
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
        self.procesar_pregunta(casilla_especial[self.__casilla])

    def procesar_pregunta(self, indice: int) -> None:
        self.__preguntas_instancia.elegir_pregunta(indice)
        self.pregunta_actual, self.__categoria = self.__preguntas_instancia.obtener_pregunta_actual()
        self.imprimir_posicion_pregunta()
        if self.verificar_respuesta():
            self.queso_instancia.conseguir_queso(self.__categoria)
            print(f'Cantidad de quesos obtenidos: {self.queso_instancia.cantidad_quesos()}')
