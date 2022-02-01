class Persona:
    def __init__(self, nombre, edad, intereses):
        self.nombre = nombre
        self.edad = edad
        self.intereses = intereses

    # Sobrecarga de métodos en acción
    def __add__(self, prg_otro_interes):
        return self.intereses + prg_otro_interes

persona_1 = Persona('Gean', 20, ['leer'])
persona_2 = Persona('Carlos', 30, ['correr', 'cocinar'])

# Sobrecarga de métodos en acción
print(persona_1 + persona_2.intereses)