class MyContextManage:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.archivo = None

    # sobreescribiendo el método
    def __enter__(self):
        print('Abrir el archivo'.center(50, '='))
        self.archivo = open(self.nombre_archivo, 'r', encoding='utf8')
        return self.archivo
    
    # sobreescribiendo el método
    def __exit__(self, tipo_excepcion, valor_excepcion, traza_error):
        if self.archivo:
            self.archivo.close()
            print('Cerrar el archivo'.center(50, '='))
