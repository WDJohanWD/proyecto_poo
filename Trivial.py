from jugador import Jugador
from Tablero import Tablero

if __name__ == "__main__":
    # Creamos dos jugadores
    jugador1 = Jugador("Jugador 1")
    jugador2 = Jugador("Jugador 2")
    
    # Creamos un tablero para cada jugador
    tablero_jugador1 = Tablero(jugador1)
    tablero_jugador2 = Tablero(jugador2)
 
    
    # Iteramos hasta que uno de los jugadores gane
    while not tablero_jugador1.queso_instancia.ha_ganado() and not tablero_jugador2.queso_instancia.ha_ganado():
        # Turno del jugador 1
        print(f"\nTurno de {jugador1.nombre}:")
        tablero_jugador1.mover()
        tablero_jugador1.posicion_pregunta()
        
        # Si el jugador 1 ganó, salimos del bucle
        if tablero_jugador1.queso_instancia.ha_ganado():
            print(f"\n¡{jugador1.nombre} ha ganado!")
            break
        
        # Turno del jugador 2
        print(f"\nTurno de {jugador2.nombre}:")
        tablero_jugador2.mover()
        tablero_jugador2.posicion_pregunta()
        
        # Si el jugador 2 ganó, salimos del bucle
        if tablero_jugador2.queso_instancia.ha_ganado():
            print(f"\n¡{jugador2.nombre} ha ganado!")
            break
