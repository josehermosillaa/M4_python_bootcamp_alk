""" Clase Volador:

Método: moverse() imprime "El pato vuela"

🔹 Clase Nadador:

Método: moverse() imprime "El pato nada"

🔹 Clase Pato:

Hereda de ambas: class Pato(Volador, Nadador)
No implementa moverse()

Qué se debe probar:


Crear un objeto Pato
Llamar a moverse()
Usar Pato.__mro__ o help(Pato) para inspeccionar el orden de búsqueda
Cambiar el orden de herencia (class Pato(Nadador, Volador)) y repetir
"""



class Volador():
    def __init__(self, altura_maxima):
        self.altura_maxima = altura_maxima


    def moverse(self):
        print("El Pato Vuela")


class Nadador:
    def __init__(self, velocidad_nado):
        self.velocidad_nado = velocidad_nado
        


    def moverse(self):
        print("El pato nada")

### EXTRA mezcla de atributos entre 2 padres y una clase hija
class Pato(Volador, Nadador):
    def __init__(self, altura_maxima, velocidad_nado):
        Volador.__init__(self, altura_maxima)
        Nadador.__init__(self, velocidad_nado)
        # self.energia = energia


        

# volador1 = Volador()

# # volador1.moverse()

pato1 = Pato(100,100)

pato1.moverse()

print(Pato.__mro__)