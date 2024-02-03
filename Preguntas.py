import json
from random import sample


class Preguntas:
    def __init__(self) -> None:
        # Lee las preguntas desde el archivo JSON
        with open('cosas No CLASES\preguntas.json', 'r', encoding='utf-8') as archivo:
            self.preguntas = json.load(archivo)

        # Inicializa las categorías disponibles
        self.categorias = list(self.preguntas.keys())
        self.categoria_actual = ''

    def elegir_pregunta(self, num: int):
        # Elegir una categoría aleatoria
        self.categoria_actual = sample(self.categorias, 1)[0]

        # Elegir una pregunta aleatoria de la categoría
        self.pregunta = sample(self.preguntas[self.categoria_actual], 1)[0]

    def obtener_pregunta_actual(self):
        return self.pregunta, self.categoria_actual
