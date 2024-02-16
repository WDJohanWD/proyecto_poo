import json
from random import sample

class Preguntas:
    preguntas: dict
    categorias: list
    categoria_actual: str
    pregunta: dict

    def __init__(self) -> None:
        #Inicializa el objeto Preguntas.
        with open('cosas No CLASES\preguntas.json', 'r', encoding='utf-8') as archivo:
            self.preguntas = json.load(archivo)

        self.categorias = list(self.preguntas.keys())
        self.categoria_actual = ''
        self.pregunta = {}

    def elegir_pregunta(self, num: int) -> None:
        #Elige una pregunta aleatoria.
        self.categoria_actual = self.categorias[num-1]
        self.pregunta = sample(self.preguntas[self.categoria_actual], 1)[0]

    def obtener_pregunta_actual(self) -> tuple:
        #Devuelve la pregunta actual y su categoría.
        return self.pregunta, self.categoria_actual
 
if __name__=='__main__':
    obt=Preguntas()
    print(len(obt.categorias))
    print(obt.categorias[1-1])
    