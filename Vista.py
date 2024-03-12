class Vista:
    
    #Métodos para el main
    def preguntar_jugador():
        
        try:
            num_jugadores = int(input('Introduce el número de jugadores: '))
        except ValueError:
            print("Por favor, introduce un número entero.")
            
        return num_jugadores

    def bucle_jugador(i):
        
        nombre = input(f'Introduce el nombre del jugador {i+1}: ')
            
        return nombre
       
    def mostrar_turno(jugadores,i):
        print(f"\nTurno de {jugadores[i].nombre}:")
     
    def mostrar_ganador(jugadores,i):
        print(f"\n¡{jugadores[i].nombre} ha ganado!") 
    
    def guardar_resultado(jugador,tablero,jugadores,tableros):
        resultados = [f"El jugador {jugador.nombre} obtuvo {tablero.queso_instancia.cantidad_quesos()}" for jugador, tablero in zip(jugadores, tableros)]
        return resultados
    
    #Métodos generales
    def errores_excepciones_general():
        print('Ha sucedido un error!!!!!!! ')
        
        
        
    #Método Clase Tablero
    def imprimir_cantidad_quesos(quesos):
        print(f'Cantidad de quesos obtenidos: {quesos}')
        
    def imprimir_pregunta(categoria,pregunta):
        print(f'\nLa categoría es {categoria}')
        print(f"\n{pregunta['enunciado']}")
        for opcion in pregunta['opciones']:
            print(opcion)