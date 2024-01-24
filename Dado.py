from random import randint


class Dado:
    num_dado: int
    #MÉTODO CONSTRUCTO
    def __init__(self) -> None:
        self.num_dado = 0

    #MÉTODO PARA ESCOGER UN NÚMERO ALEATORIO PARA EL DADO
    def lanzar_dado(self):
        self.num_dado = randint(1, 6)
        return self.num_dado


if __name__ == '__main__':
    dado = Dado()
    dado.lanzar_dado()
    print(dado.lanzar_dado())
