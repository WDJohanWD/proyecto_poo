from Tablero import Tablero
from Queso import Queso

# PyGTK, tkinter(interfaz).clases quesito, jugador, juego, tablero, dado

if __name__ == '__main__':
    tablero1 = Tablero()
    tablero1.mover()
    tablero1.posicion_pregunta()
    while tablero1.imprimir_posicion_pregunta():
        tablero1.mover()
        tablero1.posicion_pregunta()
