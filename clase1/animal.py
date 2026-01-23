"""
1. Definir una clase simple llamada Animal con atributo nombre y método hablar()
2. Crear una instancia de Animal llamada mi_gato
3. Ejecutar un método desde la instancia
4. Comprobar con isinstance() que mi_gato es una instancia de Animal
5. Mostrar que una instancia tiene vida propia y puede almacenarse, pasarse como parámetro, o guardarse en listas

📌 Objetivo: entender que una instancia es un objeto real creado a partir de una clase, y que puede verificarse con herramientas como isinstance().
"""

class Animal:
    def __init__(self,nombre):
        self.nombre = nombre
    
    def hablar(self):
        print("Guau, Miau")


mi_gato = Animal("Chimpi")
mi_gato.hablar()

print(isinstance(mi_gato,Animal)) #podemos preguntar si una instancia pertenece a la clase animal

def hacer_hablar(animal):
    animal.hablar()

hacer_hablar(mi_gato)
mi_perro = Animal("kuky")
mi_conejo = Animal("Bugs")
mi_pato = Animal("Lucas")
lista_animales = [mi_gato, mi_perro, mi_conejo,mi_pato]

for elemento in lista_animales:
    print(elemento.nombre)
    elemento.hablar()