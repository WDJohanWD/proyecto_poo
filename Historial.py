class Historial:
    
    @staticmethod
    def guardar_en_historial(resultado:str)->None:
        #Abre el archivo historial.txt para guardar los datos de las partidas.
        
        try:
            fichero = open(".\\cosas No CLASES\\historial.txt", 'w')
            fichero.write(resultado)
        except:
            print('Error al abrir o guardar el resultado  en el historial.')
