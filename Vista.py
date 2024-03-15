import time
from termcolor import colored

class Vista:
    
    #Métodos para el main
    
    def imprimir_inicio():#1

        print(colored('''
              BIENVENIDOS AL TRIVIAL:
              ''',"red", attrs=["bold"]))
        
        time.sleep(2)
        
        texto = '''
               Un Juego de Cultura General
        ¡Bienvenidos al Trivial del Queso, donde la cultura general y la estrategia 
        se combinan para alcanzar la victoria! En este emocionante juego, podrás 
        poner a prueba tus conocimientos en seis categorías diferentes: deporte, 
        geografía, arte, literatura, ciencia y entretenimiento. El objetivo es 
        ser el primer jugador en recolectar los seis quesos, uno de cada categoría,
        dispersos a lo largo del tablero de 42 casillas.'''

        print(texto)
        
        time.sleep(2)
    
    def preguntar_eleccion_inicio():#2
        eleccion = int(input('''
                         █████████████████████████████████████
                         █          ¿Qué deseas hacer?       █
                         █ 1. Comenzar a jugar directamente. █
                         █ 2. Leer primero las instrucciones.█
                         █████████████████████████████████████
                         '''))
        return eleccion
    
    def imprimir_inicio2():#3
        texto2='''Instrucciones del Juego:

        1. ''' + colored('Preparación:', 'blue') + ''' Reúne a tus amigos o familiares para formar un grupo
        de jugadores. Cada jugador seleccionará un peón y colocará su ficha
        en la casilla de inicio del tablero.

        2. ''' + colored('Turnos:', 'green') + ''' El juego comienza con el lanzamiento de un dado para determinar
        quién jugará primero. Los jugadores se turnarán en el sentido de las
        agujas del reloj. En cada turno, el jugador lanzará el dado y avanzará
        su peón esa cantidad de casillas en el tablero.

        3. ''' + colored('Categorías y Quesos:', 'yellow') + ''' A lo largo del tablero, hay seis casillas 
        especiales marcadas con los quesos de cada categoría. Por ejemplo, 
        en la casilla 7 encontrarás el queso de deporte, en la casilla 14 el 
        de geografía, y así sucesivamente (de 7 en 7 casillas). Para ganar un queso, un jugador debe
        llegar a la casilla correspondiente y responder correctamente una 
        pregunta de esa categoría.

        4. ''' + colored('Preguntas y Respuestas:', 'magenta') + ''' Cada jugador debe responder una pregunta
        de la categoría correspondiente a la casilla en la que aterrice. Si 
        la respuesta es correcta, el jugador recoge el queso y continúa su 
        turno. Si la respuesta es incorrecta, el jugador debe esperar su 
        próximo turno para intentar nuevamente.

        5. ''' + colored('Avanzar o Retroceder:', 'cyan') + ''' Además de las casillas especiales con los quesos,
        hay otras casillas en el tablero que pueden tener efectos especiales.
        Algunas casillas permiten avanzar o retroceder una cantidad específica
        de casillas, lo que puede afectar la estrategia del juego.

        6. ''' + colored('Ganar el Juego:', 'black') + ''' El primer jugador en recolectar los seis quesos, 
        uno de cada categoría, será declarado ganador del juego.

        7. ''' + colored('Cambios de Turno:', 'light_red') + ''' Si un jugador no logra responder correctamente
        una pregunta, el turno pasa al siguiente jugador en sentido de las 
        agujas del reloj.

        ''' + colored('Estrategia y Diversión:', 'light_cyan') + '''

        El Trivial del Queso no solo es un desafío de conocimientos, sino 
        también un juego de estrategia. Los jugadores deben planificar sus 
        movimientos para asegurarse de llegar a las casillas especiales con
        los quesos mientras evitan las trampas y obstáculos del tablero. 
        ¡Prepárate para un emocionante desafío de cultura general y disfruta
        compitiendo por ser el maestro del queso en este juego único!
        '''
        print(texto2)
        time.sleep(2)
    
    def preguntar_jugador():#4
        
        try:
            num_jugadores = int(input('Introduce el número de jugadores: '))
        except ValueError:
            print("Por favor, introduce un número entero.")
            
        return num_jugadores

    def bucle_jugador(i):#5
        nombre_vacio=True
        while nombre_vacio:
            nombre = input(f'Introduce el nombre del jugador {i+1}: ')
            if len(nombre) !=0:
                nombre_vacio=False
                
            else:
                nombre_vacio=True
                print('TIENES QUE PONER UN NOMBRE')
                time.sleep(1)
                
        return nombre
    
    def mostrar_cantidad_jugadores_posibles():#6
        print('La cantidad mínima de jugadores es de 2 y la cantidad máxima de jugadores es 6')
        
    def mostrar_orden_jugadores(jugadores):#7
        time.sleep(1)
        print('El orden de los jugadores se decidirá de manera aleatoria. Estos son los resultados...')
        time.sleep(2)
        lista_ordinal=['Primer','Segundo','Tercer','Cuarto','Quinto','Sexto']
        cadena=''
        for i in range(len(jugadores)):
            cadena+=f'El {lista_ordinal[i]} jugador es: {jugadores[i].nombre}  \n'
        print(cadena)
               
    def mostrar_turno(jugadores,i):#8
        time.sleep(1)
        print(f"\nTurno de {colored(jugadores[i].nombre.upper(),attrs=['underline'])}:")
        time.sleep(1)
      
    def mostrar_ganador(jugadores,i):#9
        print(f"\n¡{jugadores[i].nombre.upper()} ha ganado!") 
    
    def guardar_resultado(jugador,tablero,jugadores,tableros):#10
        resultados = [f"El jugador {jugador.nombre} obtuvo {tablero.queso_instancia.cantidad_quesos()}" for jugador, tablero in zip(jugadores, tableros)]
        return resultados
    
    def pregunta_final():#11
        final=input("¿Deseas seguir jugando? (si/no): ")
        mantener_jugadores=input('¿Deseas mantener los jugadores actuales? (si/no)')
        return final, mantener_jugadores
   
    #Métodos generales
    def errores_excepciones_general():
        texto=colored('Ha sucedido un error!!','red',attrs=['bold',])
        print(texto)
        
    def errores_excepciones_value():
        print('Introduce un valor correcto.')
        
        
    #Métodos Clase Tablero
    def preguntar_movimiento(casilla,dado):
        print('Tirando dado', end='', flush=True)
        time.sleep(0.3)
        print('.', end='', flush=True)
        time.sleep(0.3)
        print('.', end='', flush=True)
        time.sleep(0.4)
        print('.', end='\n', flush=True)
        time.sleep(2)
        
        print(f'Haz sacado un {colored(dado,'yellow',attrs=['bold'])} en el dado', flush=True)
        if casilla%7==0 and casilla!=0:
            movimiento=input(f"Estás en la casilla {colored(casilla,'yellow',attrs=['bold'])} Quieres {colored('AVANZAR (A)','green')} o {colored('RETROCEDER (R)','red')}: ").lower()
        else:
            movimiento=input(f"Estás en la casilla {casilla} Quieres {colored('AVANZAR (A)','green')} o {colored('RETROCEDER (R)','red')}: ").lower()

        return movimiento
    
    def imprimir_opcion_correcta():
        print(f"Por favor, escribe {colored('avanzar','green')} o {colored('retroceder','red')}.")
    
    def imprimir_cantidad_quesos(quesos):
        print(f'Cantidad de quesos obtenidos: {quesos}')
        
    def imprimir_pregunta(categoria,pregunta):
        
        print(f'\nLa categoría es {colored(categoria.upper(), attrs=["bold"])}')
        print(f"\n{pregunta['enunciado']}")
        for opcion in pregunta['opciones']:
            print(opcion)
    
    def pedir_respuesta():
        respuesta=input("Tu respuesta: ").lower()
        
        return respuesta
    
    #Métodos clase queso
    
    def mostrar_categoria_ganada(valor,categoria):
        if valor == 'repetido':
            print(f'Ya has ganado el queso de la categoría {categoria}. ¡Intenta en otra casilla!')
        else:
            print(f'¡Ganaste Queso de la categoría {categoria}!')
            