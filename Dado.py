from random import randint

class Dado:
    @staticmethod
    def lanzar_dado() -> int:
        #Lanza un dado y devuelve el resultado.
        return randint(1, 6)