class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.posicion = 0

    def mover(self, casillas):
        self.posicion += casillas

    def obtener_posicion(self):
        return self.posicion
