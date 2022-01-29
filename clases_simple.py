class Persona:
    def __init__(self):
        self.nombre = 'Gean Carlos'
        self.apellido = 'Baila Laurente'
        self.edad = None

class Coche:
    def __init__(self, marca, modelo, km):
        self.marca = marca
        self.modelo = modelo
        self.km = km

    def __del__(self):
        print(f'objeto Coche eliminado: {self.marca} {self.modelo} {self.km}')

class Aritmetica:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def dividir(self):
        resultado = self.a / self.b
        return '{:.4f}'.format(resultado)

    def sumar(self):
        resultado = self.a + self.b
        return '{:010d}'.format(resultado)

    def restar(self):
        return self.a - self.b
    
    def multiplicar(self):
        return self.a * self.b

persona = Persona()
print('objeto Persona:', persona.nombre, persona.apellido, persona.edad)

coche = Coche('volvo', 'v60', 500000)
print('objeto Coche:', coche.marca, coche.modelo, coche.km)

# Agregando atributos al vuelo pero OJO, es mala práctica
coche.tipo = 'sedan'
print('objeto Coche:', coche.marca, coche.modelo, coche.km, coche.tipo)

# Eliminar el objecto
del coche

aritmetica = Aritmetica(9,5)
resultado = aritmetica.dividir()
print('resultado para la división', resultado)

resultado = aritmetica.sumar()
print('resultado para la suma', resultado)

print(f'resultado para la resta {aritmetica.restar():010d}')

resultado = aritmetica.multiplicar()
print('resultado para la multiplicacion %s*%s=%010d' %(aritmetica.a, aritmetica.b, resultado,))


