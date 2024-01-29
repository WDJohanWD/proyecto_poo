import json
from random import sample


class Preguntas:

    def __init__(self, archivo='cosas No CLASES\preguntas.json') -> None:
        self.archivo = archivo
        self.preguntas = self.cargar_preguntas_desde_archivo()
        self.categoria_actual = ''
        self.preguntas_actual = []

    def cargar_preguntas_desde_archivo(self):
        with open(self.archivo, 'r') as file:
            preguntas_json = file.read()
            preguntas = json.loads(preguntas_json)
        return preguntas

    def elegir_pregunta(self, num: int):
        # Asegúrate de que num esté en el rango correcto
        num = (num - 1) % len(self.preguntas)
        self.categoria_actual = list(self.preguntas.keys())[num]
        self.preguntas_actual = list(self.preguntas[self.categoria_actual])

    def obtener_pregunta_actual(self):
        if self.preguntas_actual:
            pregunta = sample(self.preguntas_actual, 1)[0]
            # Elimina la pregunta seleccionada
            self.preguntas_actual.remove(pregunta)
            return pregunta, self.categoria_actual
        return None, None

    def imprimir_preguntas(self):
        for categoria, preguntas in self.preguntas.items():
            print(f"\nCategoría: {categoria}")
            for index, pregunta in enumerate(preguntas, start=1):
                print(f"\nPregunta {index}: {pregunta['enunciado']}")
                for opcion in pregunta['opciones']:
                    print(opcion)
                print(
                    f"Respuesta correcta: {pregunta['respuesta_correcta']}\n")


if __name__ == '__main__':
    # preg = Preguntas('cosas No CLASES\preguntas.json')
    # preg.elegir_pregunta(4)
    # print(preg.obtener_pregunta_actual())
    obj = Preguntas()
    obj.elegir_pregunta(1)
    obj.imprimir_preguntas()
