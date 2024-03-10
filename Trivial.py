from Jugador import Jugador
from Tablero import Tablero
from Historial import Historial

if __name__ == "__main__":
    while True:
        try:
            num_jugadores = int(input('Introduce el número de jugadores: '))
            
            jugadores = []
            for i in range(num_jugadores):
                nombre = input(f'Introduce el nombre del jugador {i+1}: ')
                jugadores.append(Jugador(nombre))
                
            tableros = [Tablero(jugador) for jugador in jugadores]
            
            # Iteramos hasta que uno de los jugadores gane
            while True:
                for i, tablero in enumerate(tableros):
                    print(f"\nTurno de {jugadores[i].nombre}:")
                    tablero.mover()
                    
                    # El jugador sigue avanzando mientras responde correctamente
                    while True:
                        tablero.posicion_pregunta()
                        if not tablero.verificar_respuesta():
                            break
                        tablero.mover()
                        
                    # Si el jugador ganó, salimos del bucle
                    if tablero.queso_instancia.ha_ganado():
                        print(f"\n¡{jugadores[i].nombre} ha ganado!")
                        break
                
                # Verificamos si algún jugador ha ganado
                ganador = None
                for i, tablero in enumerate(tableros):
                    if tablero.queso_instancia.ha_ganado():
                        ganador = jugadores[i]
                        break
                
                # Si hay un ganador, terminamos el juego
                if ganador:
                    resultados = [f"El jugador {jugador.nombre} obtuvo {tablero.queso_instancia.cantidad_quesos()}" for jugador, tablero in zip(jugadores, tableros)]
                    Historial.guardar_en_historial('\n'.join(resultados))
                    break
            break
        
        except ValueError:
            print("Por favor, introduce un número entero.")
        
        