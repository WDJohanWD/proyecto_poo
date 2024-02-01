from random import sample


class Preguntas:
    # DICCIONARIOS DE LAS PREGUNTAS QUE SE UTILIZARAN
    preguntas_deporte = [{
        "enunciado": "¿En qué país se originó el deporte del cricket?",
        "opciones": ["a) Inglaterra", "b) India", "c) Australia", "d) Sudáfrica"],
        "respuesta_correcta": "a"
    },
        {
        "enunciado": "¿Cuál es el deporte más popular en Brasil?",
        "opciones": ["a) Fútbol", "b) Voleibol", "c) Baloncesto", "d) Tenis"],
        "respuesta_correcta": "a"
    },
        {
        "enunciado": "¿Cuántos jugadores hay en un equipo de baloncesto durante un juego?",
        "opciones": ["a) 5", "b) 6", "c) 7", "d) 8"],
        "respuesta_correcta": "a"
    },
        {
        "enunciado": "¿En qué año se celebró la primera Copa Mundial de la FIFA?",
        "opciones": ["a) 1930", "b) 1950", "c) 1970", "d) 1990"],
        "respuesta_correcta": "a"
    },
        {
        "enunciado": "¿Quién es considerado el mejor jugador de tenis de todos los tiempos?",
        "opciones": ["a) Roger Federer", "b) Rafael Nadal", "c) Novak Djokovic", "d) Serena Williams"],
        "respuesta_correcta": "a"
    }]

    preguntas_geografia = [{
        "enunciado": "¿Cuál es el río más largo del mundo?",
        "opciones": ["a) Nilo", "b) Amazonas", "c) Yangtsé", "d) Misisipi"],
        "respuesta_correcta": "b"
    },
        {
        "enunciado": "¿En qué continente se encuentra la Gran Barrera de Coral?",
        "opciones": ["a) Asia", "b) Europa", "c) Oceanía", "d) África"],
        "respuesta_correcta": "c"
    },
        {
        "enunciado": "¿Cuál es la capital de Canadá?",
        "opciones": ["a) Ottawa", "b) Toronto", "c) Vancouver", "d) Montreal"],
        "respuesta_correcta": "a"
    },
        {
        "enunciado": "¿Cuál es la montaña más alta del mundo?",
        "opciones": ["a) Monte Everest", "b) K2", "c) Annapurna", "d) Mont Blanc"],
        "respuesta_correcta": "a"
    },
        {
        "enunciado": "¿Cuántos países conforman América del Sur?",
        "opciones": ["a) 8", "b) 10", "c) 12", "d) 14"],
        "respuesta_correcta": "c"
    }]

    preguntas_arte = [
        {
            "enunciado": "¿Quién pintó la Mona Lisa?",
            "opciones": ["a) Vincent van Gogh", "b) Leonardo da Vinci", "c) Pablo Picasso", "d) Claude Monet"],
            "respuesta_correcta": "b"
        },
        {
            "enunciado": "¿En qué país nació el pintor Salvador Dalí?",
            "opciones": ["a) España", "b) Francia", "c) Italia", "d) Alemania"],
            "respuesta_correcta": "a"
        },
        {
            "enunciado": "¿Qué movimiento artístico surgió en la década de 1950 con obras de Jackson Pollock y Willem de Kooning?",
            "opciones": ["a) Renacimiento", "b) Surrealismo", "c) Expresionismo abstracto", "d) Impresionismo"],
            "respuesta_correcta": "c"
        },
        # Agrega más preguntas de arte según sea necesario
    ]

    preguntas_literatura = [
        {
            "enunciado": "¿Quién escribió 'Cien años de soledad'?",
            "opciones": ["a) Gabriel García Márquez", "b) Mario Vargas Llosa", "c) Julio Cortázar", "d) Isabel Allende"],
            "respuesta_correcta": "a"
        },
        {
            "enunciado": "¿Cuál es la obra más famosa de William Shakespeare?",
            "opciones": ["a) Romeo y Julieta", "b) Hamlet", "c) Macbeth", "d) Otelo"],
            "respuesta_correcta": "b"
        },
        {
            "enunciado": "¿En qué país nació el escritor Franz Kafka?",
            "opciones": ["a) Alemania", "b) Austria", "c) Hungría", "d) República Checa"],
            "respuesta_correcta": "d"
        },
        # Agrega más preguntas de literatura según sea necesario
    ]

    preguntas_ciencia = [
        {
            "enunciado": "¿Cuál es el elemento más abundante en la Tierra?",
            "opciones": ["a) Oxígeno", "b) Hidrógeno", "c) Hierro", "d) Silicio"],
            "respuesta_correcta": "b"
        },
        {
            "enunciado": "¿Cuál es la unidad básica de la estructura de los seres vivos?",
            "opciones": ["a) Célula", "b) Átomo", "c) Molécula", "d) Gen"],
            "respuesta_correcta": "a"
        },
        {
            "enunciado": "¿Qué científico propuso la teoría de la relatividad?",
            "opciones": ["a) Isaac Newton", "b) Albert Einstein", "c) Galileo Galilei", "d) Stephen Hawking"],
            "respuesta_correcta": "b"
        },
        # Agrega más preguntas de ciencia según sea necesario
    ]

    preguntas_entretenimiento = [
        {
            "enunciado": "¿Cuál es la película más taquillera de todos los tiempos?",
            "opciones": ["a) Avatar", "b) Avengers: Endgame", "c) Titanic", "d) Star Wars: El despertar de la fuerza"],
            "respuesta_correcta": "b"
        },
        {
            "enunciado": "¿Quién interpretó a James Bond en 'Casino Royale'?",
            "opciones": ["a) Sean Connery", "b) Daniel Craig", "c) Pierce Brosnan", "d) Roger Moore"],
            "respuesta_correcta": "b"
        },
        {
            "enunciado": "¿En qué año se estrenó la serie de televisión 'Friends'?",
            "opciones": ["a) 1994", "b) 1996", "c) 1998", "d) 2000"],
            "respuesta_correcta": "a"
        },
        # Agrega más preguntas de entretenimiento según sea necesario
    ]

    # MÉTODO CONSTRUCTOR
    def __init__(self) -> None:
        self.pregunta = Preguntas.preguntas_deporte
        self.categoría = 'Deporte'

    # MÉTODO PARA ELEGIR EL TIPO DE PREGUNTA DEPENDIENDO DE QUE CASILLA CAE, UTILIZO EL SAMPLE PARA QUE LA PREGUNTA QUE SALGA DEL DICCIONARIO SEA ALEATORIA
    def elegir_pregunta(self, num: int):
        if num == 1:
            self.pregunta = sample(Preguntas.preguntas_literatura, 1)
            self.categoría = 'Literatura'
        elif num == 2:
            self.pregunta = sample(Preguntas.preguntas_deporte, 1)
            self.categoría = 'Deporte'
        elif num == 3:
            self.pregunta = sample(Preguntas.preguntas_geografia, 1)
            self.categoría = 'Geografía'
        elif num == 4:
            self.pregunta = sample(Preguntas.preguntas_arte, 1)
            self.categoría = 'Arte'
        elif num == 5:
            self.pregunta = sample(Preguntas.preguntas_entretenimiento, 1)
            self.categoría = 'Entretenimiento'
        else:
            self.pregunta = sample(Preguntas.preguntas_ciencia, 1)
            self.categoría = 'Ciencia'

    # MÉTODO PARA DEVOLVER LA PREGUNTA
    def obtener_pregunta_actual(self):
        return self.pregunta, self.categoría


if __name__ == '__main__':
    pass
