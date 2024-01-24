from Dado import Dado
from Queso import Queso
from Preguntas import Preguntas
from Tablero import Tablero

# PyGTK, tkinter(interfaz).clases quesito, jugador, juego, tablero, dado
class Trivial:
    

    def __init__(self):
        self.tablero=Tablero()
    
    @staticmethod   
    def jugar():
        tablero1=Tablero()
        tablero1.mover()
        while tablero1.posicion_pregunta() == True:
            tablero1.mover()

    
if __name__=='__main__':
    trivial=Trivial()
    trivial.jugar()