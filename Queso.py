class Queso:
    __quesosobtenidos: set

    def __init__(self):
        # Método constructor
        
        
        self.__quesosobtenidos = set()

    def conseguir_queso(self, categoria: str) -> bool:
        # Calcula e imprime si ha conseguido o no un queso para que no pueda conseguir dos quesos 
        # de la misma categoría
        
        
        if categoria not in self.__quesosobtenidos:
            print(f'¡Ganaste Queso de la categoría {categoria}!')
            self.__quesosobtenidos.add(categoria)
            return True
        else:
            print(f'Ya has ganado el queso de la categoría {categoria}. ¡Intenta en otra casilla!')
            return False

    def cantidad_quesos(self) -> int:
        # Devuelve la cantidad de quesos obtenidos.
        
        
        return len(self.__quesosobtenidos)

    def ha_ganado(self) -> bool:
        # Verifica si el jugador ha ganado todos los quesos disponibles.
        
        
        return len(self.__quesosobtenidos) == 6

    #Property y Setter de los atributos de la clase
    @property
    def quesos_obtenidos(self) -> set:
        return  self.__quesosobtenidas
    
    @quesos_obtenidos.setter
    def quesos_obtenidos(self, valor : set)->None:
        self.__quesosobtenidos=valor