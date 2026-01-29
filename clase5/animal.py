"""🔹 Clase base Animal:
Atributo: nombre
Método: emitir_sonido() que imprima "Sonido genérico"

🔹 Subclases Perro y Gato:
Sobrescriben emitir_sonido() para imprimir:
"Guau!" en Perro
"Miau!" en Gato
🔹 Qué se debe probar:

Crear un objeto de cada subclase

Llamar a emitir_sonido() desde cada uno

Verificar que el comportamiento es distinto, aunque el método se llama igual
"""

class Animal:
    def __init__(self, nombre:str):
        self.nombre = nombre

    def emitir_sonido(self):
        return "Sonido generico"
    
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza



    def emitir_sonido(self):
        return "Guau, Guau!"
    

        
class Gato(Animal):
    def __init__(self,nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def emitir_sonido(self):
        return "Miau, Miau!"
    

animal1 = Animal("Lagartija")

perro1 = Perro("Cachupin","Pekines")
gato1 =  Gato("Benito", "Ginger")
#polimorfismo
print(animal1.emitir_sonido())
print(perro1.emitir_sonido())
print(gato1.emitir_sonido())