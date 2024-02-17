from Dado import Dado
from Queso import Queso
from Preguntas import Preguntas
class Tablero:
    CASILLAS:int=42
    CASILLA_DEP:int=7
    CASILLA_GEO:int=14
    CASILLA_ART:int=21
    CASILLA_LIT:int=28
    CASILLA_CIE:int=35
    CASILLA_ENT:int=42
    LISTA_CASILLAS:list =[CASILLA_DEP,CASILLA_GEO,CASILLA_ART,CASILLA_LIT,CASILLA_CIE,CASILLA_ENT]
    casilla:int
    jugador:object
    preguntas_instancia:Preguntas
    queso_instancia:Queso
    categoria:str
    pregunta_actual:dict
    
    
    def __init__(self, jugador:object) -> None:
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
                self.casilla = num_movimiento % Tablero.CASILLAS
                break
            elif movimiento == 'retroceder':
                if self.casilla - dado_lanzado < 0:
                    self.casilla = Tablero.CASILLAS - (dado_lanzado - self.casilla)
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
        if self.casilla not in [Tablero.CASILLA_DEP, Tablero.CASILLA_GEO, Tablero.CASILLA_ART,
                                Tablero.CASILLA_LIT, Tablero.CASILLA_CIE, Tablero.CASILLA_ENT]:
            posicion = self.casilla % len(Tablero.LISTA_CASILLAS)
            self.preguntas_instancia.elegir_pregunta(posicion)
            self.pregunta_actual, self.categoria = self.preguntas_instancia.obtener_pregunta_actual()
            self.imprimir_posicion_pregunta()  # Llamamos a imprimir solo aquí
        else:
            self.calcular_quesos()


    def calcular_quesos(self) -> None:
        if self.casilla == Tablero.CASILLA_DEP:
            self.procesar_pregunta(1)
        elif self.casilla == Tablero.CASILLA_GEO:
            self.procesar_pregunta(2)
        elif self.casilla == Tablero.CASILLA_ART:
            self.procesar_pregunta(3)
        elif self.casilla == Tablero.CASILLA_LIT:
            self.procesar_pregunta(4)
        elif self.casilla == Tablero.CASILLA_CIE:
            self.procesar_pregunta(5)
        elif self.casilla == Tablero.CASILLA_ENT:
            self.procesar_pregunta(6)
            
    def procesar_pregunta(self, indice: int) -> None:
        self.preguntas_instancia.elegir_pregunta(indice)
        self.pregunta_actual, self.categoria = self.preguntas_instancia.obtener_pregunta_actual()
        if self.imprimir_posicion_pregunta():
            self.queso_instancia.conseguir_queso(self.categoria)
            print(f'Cantidad de quesos obtenidos: {self.queso_instancia.cantidad_quesos()}')


