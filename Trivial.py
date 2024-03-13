from Jugador import Jugador
from Tablero import Tablero
from Historial import Historial
from Vista import Vista

if __name__ == "__main__":
    while True:
        Vista.imprimir_inicio()
        num_jugadores=Vista.preguntar_jugador()
        
        
        jugadores=[]
        for i in range(num_jugadores):
            nombre = Vista.bucle_jugador(i)
            jugadores.append(Jugador(nombre))
        
          
        tableros = [Tablero(jugador) for jugador in jugadores]
        
        # Iteramos hasta que uno de los jugadores gane
        while True:
            for i, tablero in enumerate(tableros):
                
                Vista.mostrar_turno(jugadores,i)
                tablero.mover()
                
                # El jugador sigue avanzando mientras responde correctamente
                while True:
                    tablero.posicion_pregunta()
                    if not tablero.verificar_respuesta():
                        break
                    tablero.mover()
                    
                # Si el jugador ganó, salimos del bucle
                if tablero.queso_instancia.ha_ganado():
                    Vista.mostrar_ganador(jugadores,i)
                    break
             
            # Verificamos si algún jugador ha ganado
            ganador = None
            for i, tablero in enumerate(tableros):
                if tablero.queso_instancia.ha_ganado():
                    ganador = jugadores[i]
                    break
            
            # Si hay un ganador, terminamos el juego
            if ganador:
                resultados=Vista.guardar_resultado(Jugador,tablero,jugadores,tableros)
                Historial.guardar_en_historial('\n'.join(resultados))
                break
        break
    
    
    
    