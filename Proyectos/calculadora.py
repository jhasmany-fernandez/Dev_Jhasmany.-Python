class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

personas = [Persona('Juan'), Persona('María'), Persona('Juan'), Persona('Carlos')]

# Crear una instancia de Persona con nombre 'Juan' para contar
juan_temp = Persona('Juan')

# Contar cuántas veces aparece esa instancia en la lista
cantidad_juanes = personas.count(juan_temp)

print("Cantidad de veces que aparece una persona con nombre 'Juan':", cantidad_juanes)
# Salida: Cantidad de veces que aparece una persona con nombre 'Juan': 2