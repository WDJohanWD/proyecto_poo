import json
from random import sample
from Vista import Vista  # Importa la clase Vista

class Preguntas:
    __preguntas: dict  # Diccionario para almacenar las preguntas
    __categorias: list  # Lista para almacenar las categorías de preguntas
    __categoria_actual: str  # Cadena para almacenar la categoría actual
    __pregunta: dict  # Diccionario para almacenar la pregunta actual

    def __init__(self) -> None:
        # Inicializa la clase Preguntas y carga las preguntas desde un archivo JSON
        
        try:
            with open('.\\cosas No CLASES\\preguntas.json', 'r', encoding='utf-8') as archivo:
                self.__preguntas = json.load(archivo)  # Carga las preguntas desde el archivo JSON
        except:
            Vista.errores_excepciones_general()  # Maneja cualquier excepción con la clase Vista

        # Inicializa las variables de instancia
        self.__categorias = list(self.__preguntas.keys())  
        self.__categoria_actual = ''
        self.__pregunta = {}

    def elegir_pregunta(self, num: int) -> None:
        # Elige una pregunta aleatoria de una categoría específica
        
        self.__categoria_actual = self.__categorias[num-1]  # Establece la categoría actual basada en el número proporcionado
        self.__pregunta = sample(self.__preguntas[self.__categoria_actual], 1)[0]  # Elige una pregunta aleatoria de la categoría actual

    def obtener_pregunta_actual(self) -> tuple:
        # Devuelve la pregunta actual y su categoría
        
        return self.__pregunta, self.__categoria_actual

    # Propiedades y métodos para acceder y modificar las variables privadas
    
    @property
    def categoria_actual(self):
        return self.__categoria_actual

    @categoria_actual.setter
    def categoria_actual(self, valor):
        self.__categoria_actual = valor

    @property
    def pregunta(self):
        return self.__pregunta

    @pregunta.setter
    def pregunta(self, valor):
        self.__pregunta = valor
