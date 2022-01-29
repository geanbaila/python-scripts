class MiClaseBasica:
    # Varible de contexto estático
    variable_clase = 'Esto es una variable de clase'

    # Método de contexto estático
    def __init__(self, variable_instancia):
        # Varible de contexto dinámico
        self.variable_instancia = variable_instancia
        print(self.variable_instancia)

    # Método de contexto dinámico
    def acceder_variable_clase(self):
        print(self.variable_clase)
    
    # Solamente pueden acceden al contexto estático y no al dinámico
    # Método de contexto estático
    @staticmethod
    def metodo_estatico():
        print(MiClaseBasica.variable_clase)
    
    # Método de cotexto estático
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    # Método de cotexto estático
    # Por convención no se deben acceder desde fuera a métodos de la clase que se anteponen con un underscore
    @classmethod
    def _metodo_clase_2(cls):
        cls.metodo_clase()

variable_instancia = 'Esto es una variable de instancia'
mi_clase_basica = MiClaseBasica(variable_instancia)
mi_clase_basica.acceder_variable_clase()
mi_clase_basica.metodo_estatico()
MiClaseBasica.metodo_estatico()
mi_clase_basica.metodo_clase()

MiClaseBasica._metodo_clase_2()
mi_clase_basica._metodo_clase_2()


# Nota: desde el contexto dinámico sí se puede acceder al conexto estático pero no viceversa