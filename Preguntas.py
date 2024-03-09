import json
from random import sample

class Preguntas:
    __preguntas: dict
    __categorias: list
    __categoria_actual: str
    __pregunta: dict

    def __init__(self) -> None:
        #Abre el archivo donde se encuentra las preguntas y las guarda.
        
        
        with open('.\\cosas No CLASES\\preguntas.json', 'r', encoding='utf-8') as archivo:

            self.__preguntas = json.load(archivo)

        self.__categorias = list(self.__preguntas.keys())
        self.__categoria_actual = ''
        self.__pregunta = {}
    
    def elegir_pregunta(self, num: int) -> None:
        #Elige una pregunta aleatoria.
        
        
        self.__categoria_actual = self.__categorias[num-1]
        self.__pregunta = sample(self.__preguntas[self.__categoria_actual], 1)[0]

    def obtener_pregunta_actual(self) -> tuple:
        #Devuelve la pregunta actual y su categoría.
        
        
        return self.__pregunta, self.__categoria_actual
 
