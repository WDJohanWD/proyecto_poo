import time
from termcolor import colored
class Vista:
    
    
    #Métodos para el main
    def imprimir_inicio():

        print(colored('''
              BIENVENIDOS AL TRIVIAL:
              ''',"red", attrs=["bold"]))
        
        time.sleep(2)
        
        texto = '''
               Un Juego de Cultura General
        ¡Bienvenidos al Trivial del Queso, donde la cultura general y la estrategia se combinan para alcanzar la victoria! En este emocionante juego, podrás poner a prueba tus conocimientos en seis categorías diferentes: deporte, geografía, arte, literatura, ciencia y entretenimiento. El objetivo es ser el primer jugador en recolectar los seis quesos, uno de cada categoría, dispersos a lo largo del tablero de 42 casillas.

        Instrucciones del Juego:

        1. ''' + colored('Preparación:', 'blue') + ''' Reúne a tus amigos o familiares para formar un   grupo de jugadores. Cada jugador seleccionará un peón y colocará su ficha en la casilla de inicio del tablero.

        2. ''' + colored('Turnos:', 'green') + ''' El juego comienza con el lanzamiento de un dado para determinar quién jugará primero. Los jugadores se turnarán en el sentido de las agujas del reloj. En cada turno, el jugador lanzará el dado y avanzará su peón esa cantidad de casillas en el tablero.

        3. ''' + colored('Categorías y Quesos:', 'yellow') + ''' A lo largo del tablero, hay seis casillas especiales marcadas con los quesos de cada categoría. Por ejemplo, en la casilla 7 encontrarás el queso de deporte, en la casilla 14 el de geografía, y así sucesivamente. Para ganar un queso, un jugador debe llegar a la casilla correspondiente y responder correctamente una pregunta de esa categoría.

        4. ''' + colored('Preguntas y Respuestas:', 'magenta') + ''' Cada jugador debe responder una pregunta de la categoría correspondiente a la casilla en la que aterrice. Si la respuesta es correcta, el jugador recoge el queso y continúa su turno. Si la respuesta es incorrecta, el jugador debe esperar su próximo turno para intentar nuevamente.

        5. ''' + colored('Avanzar o Retroceder:', 'cyan') + ''' Además de las casillas especiales con los quesos, hay otras casillas en el tablero que pueden tener efectos especiales. Algunas casillas permiten avanzar o retroceder una cantidad específica de casillas, lo que puede afectar la estrategia del juego.

        6. ''' + colored('Ganar el Juego:', 'black') + ''' El primer jugador en recolectar los seis quesos, uno de cada categoría, será declarado ganador del juego.

        7. ''' + colored('Cambios de Turno:', 'light_red') + ''' Si un jugador no logra responder correctamente una pregunta, el turno pasa al siguiente jugador en sentido de las agujas del reloj.

        ''' + colored('Estrategia y Diversión:', 'light_cyan') + '''

        El Trivial del Queso no solo es un desafío de conocimientos, sino también un juego de estrategia. Los jugadores deben planificar sus movimientos para asegurarse de llegar a las casillas especiales con los quesos mientras evitan las trampas y obstáculos del tablero. ¡Prepárate para un emocionante desafío de cultura general y disfruta compitiendo por ser el maestro del queso en este juego único!
        '''
        
        print(texto)
    
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
    def preguntar_movimiento(casilla,dado):
        movimiento=input(f'Estás en la casilla {casilla} Quieres AVANZAR o RETROCEDER: {dado} casillas ').lower()
        return movimiento
    
    def imprimir_opcion_correcta():
        print("Por favor, escribe 'avanzar' o 'retroceder'.")
    
    def imprimir_cantidad_quesos(quesos):
        print(f'Cantidad de quesos obtenidos: {quesos}')
        
    def imprimir_pregunta(categoria,pregunta):
        print(f'\nLa categoría es {categoria}')
        print(f"\n{pregunta['enunciado']}")
        for opcion in pregunta['opciones']:
            print(opcion)
    
    def pedir_respuesta():
        respuesta=input("Tu respuesta: ").lower()
        
        return respuesta
    