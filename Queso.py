class Queso:
    categoria: str
    quesos_obtenidos: set

    def __init__(self):
        # Método constructor
        self._categoria = ''
        self.__quesos_obtenidos = set()

    def conseguir_queso(self, categoria: str) -> bool:
        # Calcula e imprime si ha conseguido o no un queso para que no pueda conseguir dos quesos 
        # de la misma categoría
        
        self._categoria = categoria
        if categoria not in self.__quesos_obtenidos:
            print(f'¡Ganaste Queso de la categoría {categoria}!')
            self.__quesos_obtenidos.add(categoria)
            return True
        else:
            print(f'Ya has ganado el queso de la categoría {categoria}. ¡Intenta en otra casilla!')
            return False

    def cantidad_quesos(self) -> int:
        # Devuelve la cantidad de quesos obtenidos.
        return len(self.__quesos_obtenidos)

    def ha_ganado(self) -> bool:
        # Verifica si el jugador ha ganado todos los quesos disponibles.
        return len(self.__quesos_obtenidos) == 6
