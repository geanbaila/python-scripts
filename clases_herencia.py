class Figura:
    def __init__(self, base, alto):
        self.base = base
        self.alto = alto

class Color:
    def __init__(self, color):
        self.color = color

class Rectangulo (Figura, Color):
    def __init__(self, base, alto, color):
        Figura.__init__(self, base, alto)
        Color.__init__(self, color)

    def area(self):
        print (self.base * self.alto, self.color)

rectangulo = Rectangulo(5, 10, 'rojo')
rectangulo.area()
print('Method Resolution Order:', Rectangulo.mro())