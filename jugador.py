class Jugador:
    nombre: str
    posicion:int
    
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.__posicion = 0
    
    @property
    def posicion(self):
        return self.__posicion
    
    @posicion.setter
    def posicion(self,nueva_posicion):
        self.__posicion=nueva_posicion
    
    def mover(self, casillas:int):
        self.__posicion += casillas

    def obtener_posicion(self):
        return self.__posicion
