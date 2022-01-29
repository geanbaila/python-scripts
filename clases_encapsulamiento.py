class Persona:
    def __init__(self, nombre, apellido, edad):
        # No se te permite saltar el encapsulamiento. Es mala práctica por convención
        self.__nombre = nombre
        # No se te permite saltar el encapsulamiento. Es mala práctica por convención
        self.__apellido = apellido
        # Se te permite saltar el encapsulamiento pero no debes. Es mala práctica por convención
        self._edad = edad

    # Decorador para getter
    @property
    def nombre(self):
        return self.__nombre
    
    # Decorador para setter
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    # Getter tradicional
    def getApellido(self):
        return self.__apellido
    
    # Setter tradicional
    def setApellido(self, apellido):
        self.__apellido = apellido

    # Decimos que es una variable de solo lectura porque no tiene un setter
    def getEdad(self):
        return self._edad


persona = Persona('Gean', 'Baila', 30)

# Modificamos la variable de instancia a través del setter decorador. Buena práctica
persona.nombre = 'Carlos'
print(persona.nombre)

# Mala práctica. Ha intentado modificar la variable de instancia directamente pero se ha evitado porque usó un setter y getter decorador
persona.__nombre = 'Gean Carlos'
print(persona.nombre)

persona.setApellido('Baila Laurente')
print(persona.getApellido())

'''
Por convención, modifica el valor de variables con prefijo underscore (_edad o __edad) 
a través del encapsulamiento, caso contrario es mala práctica.
'''
persona._edad = 100
print(persona._edad)