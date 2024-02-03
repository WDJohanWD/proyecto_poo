from random import randint


class Dado:

    # MÉTODO CONSTRUCTO
    def __init__(self) -> None:
        pass

    # MÉTODO PARA ESCOGER UN NÚMERO ALEATORIO PARA EL DADO
    @staticmethod
    def lanzar_dado():
        return randint(1, 6)


if __name__ == '__main__':
    dado = Dado()
    dado.lanzar_dado()
    print(dado.lanzar_dado())
