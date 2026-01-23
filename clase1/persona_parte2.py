"""
1. Reutilizar la clase Persona con atributos nombre y edad
2. Crear dos objetos distintos: persona1 y persona2
3. Ver cómo cada objeto tiene su estado individual
4. Modificar el atributo edad de uno de los objetos
5. Verificar que los cambios en un objeto no afectan al otro
6. Agregar un nuevo atributo "profesión" directamente a uno de los objetos
7. Mostrar que no todos los objetos tienen por qué tener los mismos atributos si se agregan dinámicamente
"""


class Persona():
    #1 2
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    #3
    def presentarse(self):
        print(f"Hola bienvenido soy {self.nombre}, tengo {self.edad}, mucho gusto")

    def cumplir_anios(self):
        # self.edad = self.edad + 1
        self.edad += 1
        print("Feliz cumpleaños!")
#4
juan = Persona("Juan", 25)
emilia = Persona("Emilia",18)
#5
juan.presentarse()
emilia.presentarse()

# #crear una funcion para cumplir aaños
# juan.cumplir_anios()
# juan.presentarse()

#cambio del atributo 
juan.edad = 10
juan.presentarse()

#agregar profesion
emilia.profesion = "Enfermera"

print(emilia.profesion)
print(juan.profesion)

