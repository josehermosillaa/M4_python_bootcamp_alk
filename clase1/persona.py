"""
1. Definir una clase Persona con el método especial __init__()
2. Asignar atributos: nombre, edad
3. Crear el método presentarse() que imprima una presentación
4. Instanciar dos objetos diferentes con datos propios
5. Ejecutar el método presentarse() desde cada objeto
6. Ver cómo cada objeto mantiene su propio estado
7. Bonus: Agregar otro método, como cumplir_anios() que sume 1 a la edad
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

#crear una funcion para cumplir aaños
juan.cumplir_anios()
juan.presentarse()
