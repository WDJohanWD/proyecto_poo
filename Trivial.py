from Jugador import Jugador
from Tablero import Tablero
from Historial import Historial
from Vista import Vista
from random import sample

if __name__ == "__main__":
    jugar_de_nuevo=True
    mantener_jugadores=False
    while jugar_de_nuevo:
        Vista.imprimir_inicio()
        eleccion_inicio=Vista.preguntar_eleccion_inicio()
        if eleccion_inicio == 1:
            pass
        elif eleccion_inicio ==2:
            Vista.imprimir_inicio2()
        if mantener_jugadores ==False:
            jugadores=[]
            while True:
                try:
                    num_jugadores=Vista.preguntar_jugador()
                    if num_jugadores>= 2 and num_jugadores <=6:
                        for i in range(num_jugadores):
                            nombre = Vista.bucle_jugador(i)
                            jugadores.append(Jugador(nombre))
                        break
                    else:
                        Vista.mostrar_cantidad_jugadores_posibles()
                except ValueError:
                    Vista.errores_excepciones_value()
                except:
                    Vista.errores_excepciones_general
        
        jugadores=sample(jugadores,num_jugadores)
        Vista.mostrar_orden_jugadores(jugadores)
        
        
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
            
        final, mantener_jugadores=Vista.pregunta_final()
        
        if final.lower() =='si':
            jugar_de_nuevo=True
        else:
            jugar_de_nuevo=False
        
        if mantener_jugadores.lower() == 'si':
            mantener_jugadores=True
        else:
            mantener_jugadores=False
    
    
    
    