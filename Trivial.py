from Jugador import Jugador
from Tablero import Tablero
from Historial import Historial
from Vista import Vista
from random import sample

class Trivial:
    def trivial_main():
        
        jugar_de_nuevo=True #Bandera de jugar de nuevo para preguntar al final al jugador si quiere volver a jugar
        mantener_jugadores=False #Bander de mantener jugadores para preguntar al final al jugador si quiere mantener los jugadores anteriores
        
        #Bucle principal del juevo
        while jugar_de_nuevo:
            
            Vista.imprimir_inicio() #Bienvenida
            eleccion_inicio=Vista.preguntar_eleccion_inicio() #Pregunta si jugar directamente o mirar las instrucciones
            if eleccion_inicio == 1:
                pass
            elif eleccion_inicio ==2:
                Vista.imprimir_inicio2()
                
            if mantener_jugadores ==False:
            #Crea jugadores
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
            
            
            jugadores=sample(jugadores,num_jugadores) #Elige al azar el orden de los jugadores
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
                
            final, mantener_jugadores=Vista.pregunta_final() #Preguntas  si quiere seguir jugando o cerrar el programa y si quiere mantener jugadores
            
            if final.lower() =='si':
                jugar_de_nuevo=True
            else:
                jugar_de_nuevo=False
            
            if mantener_jugadores.lower() == 'si':
                mantener_jugadores=True
            else:
                mantener_jugadores=False