from Preguntas import Preguntas


class Queso:
    def __init__(self):
        self.preguntas = Preguntas()
        self.quesos_obtenidos = set()

    def conseguir_queso(self, categoria):
        if categoria not in self.quesos_obtenidos:
            print(f'¡Ganaste Queso de la categoría {categoria}!')
            self.quesos_obtenidos.add(categoria)
            return True
        else:
            print(f'Ya has ganado el queso de la categoría {categoria}. ¡Intenta en otra casilla!')
            return False

    def cantidad_quesos(self):
        return len(self.quesos_obtenidos)

    def ha_ganado(self):
        return len(self.quesos_obtenidos) == len(self.preguntas.categorias)


# Ejemplo de uso:
if __name__ == '__main__':
    queso = Queso()

    # Intenta ganar un queso de la categoría 'Deporte'
    queso.conseguir_queso('Deporte')

    # Intenta ganar otro queso de la misma categoría, debería mostrar un mensaje indicando que ya lo ganó
    queso.conseguir_queso('Deporte')

    # Verifica la cantidad de quesos obtenidos (debería ser 1 en este punto)
    print(f'Cantidad de quesos obtenidos: {queso.cantidad_quesos()}')

    # Verifica si ha ganado el juego (debería ser False en este punto)
    print(f'¿Ha ganado el juego? {queso.ha_ganado()}')

    # Intenta ganar quesos de otras categorías para completar los 6 quesos
    queso.conseguir_queso('Geografía')
    queso.conseguir_queso('Arte')
    queso.conseguir_queso('Literatura')
    queso.conseguir_queso('Ciencia')
    queso.conseguir_queso('Entretenimiento')

    # Verifica nuevamente si ha ganado el juego (debería ser True en este punto)
    print(f'¿Ha ganado el juego? {queso.ha_ganado()}')
