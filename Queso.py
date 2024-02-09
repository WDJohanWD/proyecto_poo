class Queso:
    categoria: str
    quesos_obtenidos:set
    def __init__(self):
        self.categoria = ''
        self.quesos_obtenidos = set()

    def conseguir_queso(self, categoria:str):
        self.categoria = categoria
        if categoria not in self.quesos_obtenidos:
            print(f'¡Ganaste Queso de la categoría {categoria}!')
            self.quesos_obtenidos.add(categoria)
            return True
        else:
            print(f'Ya has ganado el queso de la categoría {categoria}. ¡Intenta en otra casilla!')
            return False

    def cantidad_quesos(self):
        return len(self.quesos_obtenidos)

    def ha_ganado(self):
        return len(self.quesos_obtenidos) == len(self.categoria)
