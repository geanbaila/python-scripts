from abc import ABC, abstractclassmethod

# Extender de ABC te convierte en clase abstracta
class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    # El decorador converte a un método abstracto. no incluye cuerpo
    @abstractclassmethod
    def calcular_area(self):
        pass

class Rectangulo(FiguraGeometrica):
    # Se inicializan las variables de instancia
    def __init__(self, ancho, alto):
        # Usamos super por tratarse de una herencia simple (no herencia múltiple)
        super().__init__(ancho, alto)
    
    # Se implementa el método abstracto
    def calcular_area(self):
        return self.ancho * self.alto

# Las clases abstractas no pueden ser instanciadas por eso instanciamos desde Rectangulo
rectangulo = Rectangulo(5, 10)
print(f'El área del rectángulo es: {rectangulo.calcular_area()}')