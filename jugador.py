class Jugador:
    nombre: str
    posicion:int
    
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.posicion = 0

    def mover(self, casillas:int):
        self.posicion += casillas

    def obtener_posicion(self):
        return self.posicion
