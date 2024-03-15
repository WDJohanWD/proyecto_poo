from Vista import Vista
class Historial:
    RUTA=".\\cosas No CLASES\\historial.txt"
    
    @staticmethod
    def guardar_en_historial(resultado:str)->None:
        #Abre el archivo historial.txt para guardar los datos de las partidas.
        
        try:
            fichero = open(Historial.RUTA, 'w')
            fichero.write(resultado)
        except:
            Vista.errores_excepciones_general()
