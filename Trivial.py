from Jugador import Jugador
from Tablero import Tablero
from Historial import Historial

if __name__ == "__main__":
    
    nombre1 = input('Introduce el nombre del jugador 1: ')
    nombre2 = input('Introduce el nombre del jugador 2: ')
    
    # Creamos dos jugadores
    jugador1 = Jugador(nombre1)
    jugador2 = Jugador(nombre2)
    
    # Creamos un tablero para cada jugador
    tablero_jugador1 = Tablero(jugador1)
    tablero_jugador2 = Tablero(jugador2)
 
    
    # Iteramos hasta que uno de los jugadores gane
    while not tablero_jugador1.queso_instancia.ha_ganado() and not tablero_jugador2.queso_instancia.ha_ganado():
        # Turno del jugador 1
        print(f"\nTurno de {jugador1.nombre}:")
        tablero_jugador1.mover()
        
        # El jugador 1 sigue avanzando mientras responde correctamente
        while True:
            tablero_jugador1.posicion_pregunta()
            if not  tablero_jugador1.verificar_respuesta():
                break
            tablero_jugador1.mover()
        
        # Si el jugador 1 ganó, salimos del bucle
        if tablero_jugador1.queso_instancia.ha_ganado():
            print(f"\n¡{jugador1.nombre} ha ganado!")
            break
        
        # Turno del jugador 2
        print(f"\nTurno de {jugador2.nombre}:")
        tablero_jugador2.mover()
        
        # El jugador 2 sigue avanzando mientras responde correctamente
        while True:
            tablero_jugador2.posicion_pregunta()
            if not tablero_jugador2.verificar_respuesta():
                break
            tablero_jugador2.mover()
        
        # Si el jugador 2 ganó, salimos del bucle
        if tablero_jugador2.queso_instancia.ha_ganado():
            print(f"\n¡{jugador2.nombre} ha ganado!")
            break
    
    resultado= f"El jugador {jugador1} obtuvo {tablero_jugador1.queso_instancia.cantidad_quesos()} y el jugador {jugador2} obtuvo {tablero_jugador2.queso_instancia.cantidad_quesos()}"
    Historial.guardar_en_historial(resultado)