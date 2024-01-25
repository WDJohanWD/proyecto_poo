import json


def cargar_preguntas_desde_archivo(archivo):
    with open(archivo, 'r') as file:
        preguntas_json = file.read()
        preguntas = json.loads(preguntas_json)
    return preguntas


# Especifica la ruta de tu archivo
archivo_preguntas = 'cosas No CLASES\preguntas.json'

# Carga las preguntas desde el archivo
preguntas = cargar_preguntas_desde_archivo(archivo_preguntas)

# Ahora, 'preguntas' es una lista de diccionarios que puedes usar en tu programa
print(preguntas)
