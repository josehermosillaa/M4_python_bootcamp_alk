"""Qué debe tener la clase Persona:

Atributos: nombre, edad
Método: presentarse() que imprima una presentación básica

🔹 Qué debe tener la subclase Empleado:
Atributo adicional: cargo
Método sobrescrito presentarse() que además incluya el cargo
Método adicional: trabajar() que imprima lo que hace
"""

class Persona:
    def __init__(self, nombre:str, edad:int):

        self.nombre = nombre #en Javascript, TypeScript se puede agregar tipado fuerte
        self.edad = edad
    
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
        # return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."



#la subclase empleado hereda de persona


class Empleado(Persona):
    def __init__(self, nombre, edad, cargo, sueldo):
        super().__init__(nombre, edad)
        self.cargo = cargo
        self.sueldo = sueldo
        
    #aqui estamos sobreescribniendo el metodo presentarse de la clase padre o super clase
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, y tengo {self.edad} años, trabajo como {self.cargo} y mi sueldo es de ${self.sueldo}")
    
    def trabajar(self):
        print(f"mi cargo es {self.cargo}")


persona1 = Persona("Ana", 30)
empleado1 = Empleado("Carlos",40, "Analista", 1200000)

persona1.presentarse()
empleado1.presentarse()
empleado1.trabajar()