from Vista import Vista
class Queso:
    __quesos_obtenidos: set
    NUEVO='nuevo'
    REPETIDO='repetido'
    def __init__(self):
        # Método constructor
        
        
        self.__quesos_obtenidos = set()

    def conseguir_queso(self, categoria: str) -> bool:
        # Calcula e imprime si ha conseguido o no un queso para que no pueda conseguir dos quesos 
        # de la misma categoría
        
        
        if categoria not in self.__quesos_obtenidos:
            Vista.mostrar_categoria_ganada(Queso.NUEVO,categoria)
            self.__quesos_obtenidos.add(categoria)
            return True
        else:
            Vista.mostrar_categoria_ganada(Queso.REPETIDO,categoria)
            return False

    def cantidad_quesos(self) -> int:
        # Devuelve la cantidad de quesos obtenidos.
        
        
        return len(self.__quesos_obtenidos)

    def ha_ganado(self) -> bool:
        # Verifica si el jugador ha ganado todos los quesos disponibles.
        
        
        return len(self.__quesos_obtenidos) == 6

    #Property y Setter de los atributos de la clase
    @property
    def quesos_obtenidos(self) -> set:
        return  self.__quesos_obtenidos
    
    @quesos_obtenidos.setter
    def quesos_obtenidos(self, valor : set)->None:
        self.__quesos_obtenidos=valor