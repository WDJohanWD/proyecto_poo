
class Queso:
    categoria: str
    quesos_obtenidos: set

    def __init__(self):
        #Método constructor
        self.categoria = ''
        self.quesos_obtenidos = set()

    def conseguir_queso(self, categoria: str) -> bool:
        #Calcula e imprime si ha conseguido o no un queso para que no pueda conseguir dos quesos 
        #de la misma categoría
        
        self.categoria = categoria
        if categoria not in self.quesos_obtenidos:
            print(f'¡Ganaste Queso de la categoría {categoria}!')
            self.quesos_obtenidos.add(categoria)
            return True
        else:
            print(f'Ya has ganado el queso de la categoría {categoria}. ¡Intenta en otra casilla!')
            return False

    def cantidad_quesos(self) -> int:
        #Devuelve la cantidad de quesos obtenidos.
        return len(self.quesos_obtenidos)

    def ha_ganado(self) -> bool:
        # Verifica si el jugador ha ganado todos los quesos disponibles.
        
        return len(self.quesos_obtenidos) == 6

