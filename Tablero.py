from Dado import Dado
from Queso import Queso
from Preguntas import Preguntas
from Vista import Vista  

class Tablero:
    # Atributos de la clase Tablero
    __casilla: int  # Casilla actual del jugador
    __jugador: object  # Objeto del jugador actual
    __preguntas_instancia: Preguntas  # Instancia de la clase Preguntas
    __pregunta_actual: dict  # Pregunta actual en el tablero
    __categoria: str  # Categoría de la pregunta actual
    queso_instancia: Queso  # Instancia de la clase Queso
    __respuesta_usuario: str  # Respuesta del usuario a la pregunta

    # Constantes de clase
    CASILLAS: int = 42  # Número total de casillas en el tablero
    CASILLA_DEP: int = 7  # Número de casilla de la categoría DEPORTE
    CASILLA_GEO: int = 14  # Número de casilla de la categoría GEOGRAFÍA
    CASILLA_ART: int = 21  # Número de casilla de la categoría ARTE
    CASILLA_LIT: int = 28  # Número de casilla de la categoría LITERATURA
    CASILLA_CIE: int = 35  # Número de casilla de la categoría CIENCIA
    CASILLA_ENT: int = 42  # Número de casilla de la categoría ENTRETENIMIENTO
    LISTA_CASILLAS: list = [CASILLA_DEP, CASILLA_GEO, CASILLA_ART, CASILLA_LIT, CASILLA_CIE, CASILLA_ENT]  # Lista de casillas con preguntas especiales

    def __init__(self, jugador: object) -> None:
        # Constructor de la clase Tablero que inicializa los atributos
        
        self.__casilla = 0  # Inicializa la casilla del jugador en 0
        self.__jugador = jugador  # Asigna el jugador actual
        self.__preguntas_instancia = Preguntas()  # Inicializa una instancia de la clase Preguntas
        self.__pregunta_actual = {}  # Inicializa la pregunta actual como un diccionario vacío
        self.__categoria = ''  # Inicializa la categoría como una cadena vacía
        self.queso_instancia = Queso()  # Inicializa una instancia de la clase Queso
        self.__respuesta_usuario = ''  # Inicializa la respuesta del usuario como una cadena vacía

    def mover(self) -> None:
        # Método para moverse por el tablero y realizar acciones en cada casilla
        
        dado = Dado()  # Crea un objeto Dado
        dado_lanzado = dado.lanzar_dado()  # Obtiene el valor del dado lanzado
        while True:
            try:
                movimiento = Vista.preguntar_movimiento(self.__casilla, dado_lanzado)  # Pregunta al jugador si quiere avanzar o retroceder
                if movimiento == 'avanzar' or movimiento == 'a':  # Si elige avanzar
                    num_movimiento = self.__casilla + dado_lanzado  # Calcula la nueva casilla
                    if num_movimiento == Tablero.CASILLAS:
                        self.__casilla = num_movimiento
                    else:
                        self.__casilla = num_movimiento % Tablero.CASILLAS  # Calcula la nueva casilla considerando el número total de casillas
                    break
                elif movimiento == 'retroceder' or movimiento == 'r':  # Si elige retroceder
                    if self.__casilla - dado_lanzado < 0:
                        self.__casilla = Tablero.CASILLAS + 1 - (dado_lanzado - self.__casilla)
                    else:
                        self.__casilla -= dado_lanzado  # Retrocede el número de casillas indicado
                    break
                else:
                    Vista.imprimir_opcion_correcta()  # Si la opción ingresada no es válida, muestra un mensaje
            except ValueError:
                Vista.errores_excepciones_general()  # Si ocurre un error, muestra un mensaje de error general

    def imprimir_posicion_pregunta(self) -> None:
        # Método para imprimir la pregunta actual en la posición del jugador
        
        if self.__pregunta_actual:
            Vista.imprimir_pregunta(self.__categoria, self.__pregunta_actual)  # Imprime la pregunta y la categoría
            self.__respuesta_usuario = Vista.pedir_respuesta()  # Pide al usuario su respuesta

    def verificar_respuesta(self) -> bool:
        # Método para verificar si la respuesta del usuario es correcta
        
        return self.__respuesta_usuario == self.__pregunta_actual['respuesta_correcta']  # Compara la respuesta del usuario con la respuesta correcta

    def posicion_pregunta(self) -> None:
        # Método para determinar la posición de la pregunta en el tablero y realizar las acciones correspondientes
        
        if self.__casilla not in Tablero.LISTA_CASILLAS:  # Si la casilla no es especial
            posicion = self.__casilla % len(Tablero.LISTA_CASILLAS)  # Calcula la posición de la pregunta
            self.__preguntas_instancia.elegir_pregunta(posicion)  # Elige una pregunta basada en la posición
            self.__pregunta_actual, self.__categoria = self.__preguntas_instancia.obtener_pregunta_actual()  # Obtiene la pregunta actual y su categoría
            self.imprimir_posicion_pregunta()  # Imprime la pregunta
        else:
            self.calcular_quesos()  # Si la casilla es especial, calcula los quesos

    def calcular_quesos(self) -> None:
        # Método para calcular los quesos en el tablero
        
        casilla_especial = {  # Diccionario que asigna cada casilla especial a su índice
            Tablero.CASILLA_DEP: 1,
            Tablero.CASILLA_GEO: 2,
            Tablero.CASILLA_ART: 3,
            Tablero.CASILLA_LIT: 4,
            Tablero.CASILLA_CIE: 5,
            Tablero.CASILLA_ENT: 6
        }
        self.procesar_pregunta(casilla_especial[self.__casilla])  # Procesa la pregunta según la casilla especial

    def procesar_pregunta(self, indice: int) -> None:
        # Método para procesar la pregunta
        
        self.__preguntas_instancia.elegir_pregunta(indice)  # Elige una pregunta basada en el índice proporcionado
        self.__pregunta_actual, self.__categoria = self.__preguntas_instancia.obtener_pregunta_actual()  # Obtiene la pregunta actual y su categoría
        self.imprimir_posicion_pregunta()  # Imprime la pregunta
        if self.verificar_respuesta():  # Verifica si la respuesta del usuario es correcta
            self.queso_instancia.conseguir_queso(self.__categoria)  # Incrementa el queso correspondiente
            Vista.imprimir_cantidad_quesos(self.queso_instancia.cantidad_quesos())  # Imprime la cantidad de quesos

    # Propiedades y setters de los atributos privados
    @property
    def casilla(self) -> int:
        return self.__casilla

    @casilla.setter
    def casilla(self, valor: int) -> None:
        self.__casilla = valor

    @property
    def jugador(self) -> object:
        return self.__jugador

    @jugador.setter
    def jugador(self, valor: object) -> None:
        self.__jugador = valor

    @property
    def preguntas_instancia(self) -> Preguntas:
        return self.__preguntas_instancia

    @preguntas_instancia.setter
    def preguntas_instancia(self, valor: Preguntas) -> None:
        self.__preguntas_instancia = valor

    @property
    def pregunta_actual(self) -> dict:
        return self.__pregunta_actual

    @pregunta_actual.setter
    def pregunta_actual(self, valor: dict) -> None:
        self.__pregunta_actual = valor

    @property
    def categoria(self) -> str:
        return self.__categoria

    @categoria.setter
    def categoria(self, valor: str) -> None:
        self.__categoria = valor

    @property
    def respuesta_usuario(self) -> str:
        return self.__respuesta_usuario

    @respuesta_usuario.setter
    def respuesta_usuario(self, valor: str) -> None:
        self.__respuesta_usuario = valor
