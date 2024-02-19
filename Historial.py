class Historial:
    @staticmethod
    def guardar_en_historial(resultado):
        fichero = open(".\\cosas No CLASES\\historial.txt", 'a')
        fichero.write(resultado)
