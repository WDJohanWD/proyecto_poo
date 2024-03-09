from Dado import Dado
from Queso import Queso
from Preguntas import Preguntas

class Tablero:
    # Atributos de la clase tablero
    __casilla: int
    jugador: object
    __preguntas_instancia: Preguntas
    __pregunta_actual: dict
    __categoria: str 
    queso_instancia: Queso 
    __respuesta_usuario:str
    
    #Constantes de clase
    CASILLAS: int = 42
    CASILLA_DEP: int = 7
    CASILLA_GEO: int = 14
    CASILLA_ART: int = 21
    CASILLA_LIT: int = 28
    CASILLA_CIE: int = 35
    CASILLA_ENT: int = 42
    LISTA_CASILLAS: list = [CASILLA_DEP, CASILLA_GEO, CASILLA_ART, CASILLA_LIT, CASILLA_CIE, CASILLA_ENT]
    
    def __init__(self, jugador: object) -> None:
        #Constructor que solo recibe el jugador  actual, y crea una instancia de
        #las clases Queso y Preguntas.
        
        
        self.__casilla  = 0
        self.jugador  = jugador
        self.__preguntas_instancia = Preguntas()
        self.__pregunta_actual = {}
        self.__categoria = ''
        self.queso_instancia = Queso()
        self.__respuesta_usuario=''

    def mover(self) -> None:
        #Método utilizado para moverse  por el tablero y realizar acciones en 
        #cada casilla. Con la opción de avanzar o retroceder y también utiliza
        #un try/except para regular la entrada de datos.
        
        
        dado: Dado = Dado()
        dado_lanzado: int = dado.lanzar_dado()
        while True:
            try:
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
            except ValueError:
                print('Valor incorrecto. Por favor, escriba "avanzar" o "retroceder".')

    def imprimir_posicion_pregunta(self):
        #Método utilizado para imprimir un diccionario (preguntas) de manera que
        #se vea bien  en la terminal.
        
        
        if self.__pregunta_actual:
            print(f'\nLa categoría es {self.__categoria}')
            print(f"\n{self.__pregunta_actual['enunciado']}")
            for opcion in self.__pregunta_actual['opciones']:
                print(opcion)

            self.__respuesta_usuario: str = input("Tu respuesta: ").lower()
            
    def verificar_respuesta(self)-> bool:
        #Verifica si la respuesta  del usuario coincide con la respuesta real.
        
        
        return self.__respuesta_usuario == self.__pregunta_actual['respuesta_correcta']
        
    def posicion_pregunta(self) -> None:
        #Separa las casillas que tienen queso y las que no, donde las que no 
        #tienen quesos, elige una categoria dependiendo del numero de la casilla
        #y en las que tienen queso, se llama a otro método
        
        
        if self.__casilla not in Tablero.LISTA_CASILLAS:
            posicion: int = self.__casilla % len(Tablero.LISTA_CASILLAS)
            self.__preguntas_instancia.elegir_pregunta(posicion)
            self.__pregunta_actual, self.__categoria = self.__preguntas_instancia.obtener_pregunta_actual()
            self.imprimir_posicion_pregunta()
        else:
            self.calcular_quesos()

    def calcular_quesos(self) -> None:
        #Establece la categoría de cada una de las casillas donde hay queso y 
        # utiliza otro método para imprimir la pregunta.
        
        
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
        #Método para procesar la pregunta del Queso, imprimiento si ha ganado el 
        # queso y cuantos tiene.
        
        
        self.__preguntas_instancia.elegir_pregunta(indice)
        self.__pregunta_actual, self.__categoria = self.__preguntas_instancia.obtener_pregunta_actual()
        self.imprimir_posicion_pregunta()
        if self.verificar_respuesta():
            self.queso_instancia.conseguir_queso(self.__categoria)
            print(f'Cantidad de quesos obtenidos: {self.queso_instancia.cantidad_quesos()}')

    #Property y Setter de los atributos privados
    @property
    def casilla(self):
        return self.__casilla

    @casilla.setter
    def casilla(self, valor):
        self.__casilla = valor

    @property
    def jugador(self):
        return self.__jugador

    @jugador.setter
    def jugador(self, valor):
        self.__jugador = valor

    @property
    def preguntas_instancia(self):
        return self.__preguntas_instancia

    @preguntas_instancia.setter
    def preguntas_instancia(self, valor):
        self.__preguntas_instancia = valor

    @property
    def pregunta_actual(self):
        return self.__pregunta_actual

    @pregunta_actual.setter
    def pregunta_actual(self, valor):
        self.__pregunta_actual = valor

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, valor):
        self.__categoria = valor

    @property
    def respuesta_usuario(self):
        return self.__respuesta_usuario

    @respuesta_usuario.setter
    def respuesta_usuario(self, valor):
        self.__respuesta_usuario = valor