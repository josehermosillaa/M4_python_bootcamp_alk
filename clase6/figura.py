"""
Clase base Figura:
Método dibujar() (vacío o con pass)
Subclases:
Rectangulo: sobrescribe dibujar() con "Dibujo un rectángulo"
Circulo: sobrescribe dibujar() con "Dibujo un círculo"
Triangulo: sobrescribe dibujar() con "Dibujo un triángulo"

🔹 Qué se debe probar:

Crear una lista con objetos de distintas figuras

Iterar con un for y llamar a dibujar()

Verificar que cada objeto ejecuta su propia versión del método

"""


class Figura:
    def __init__(self, ancho):
        self.ancho = ancho
    
    def dibujar(self):
        pass

    def calcular_area(self):
        pass

class Rectangulo(Figura):

    def __init__(self, ancho, largo):
        super().__init__(ancho)
        self.largo =  largo

    def dibujar(self):
        print("Se dibuja un rectangulo")

    def calcular_area(self):
        return self.largo * self.ancho
    
class Circulo(Figura):
    PI = 3.14

    def __init__(self, ancho):
        #asumiremos que ancho es el diametro en este caso
        super().__init__(ancho)
    
    def dibujar(self):
        print("Dibujamos un circulo")
    
    def calcular_area(self):
        return (self.PI**2)*(self.ancho/2)
    
class Triangulo(Figura):
    #asumimos ancho como la base del trriangulo
    def __init__(self, ancho, altura):
        super().__init__(ancho)
        self.altura = altura

    def dibujar(self):
        print("Se dibuja un triangulo")

    def calcular_area(self):
        return self.ancho * self.altura/2
    
rectangulo1 = Rectangulo(3,2)

circulo1 = Circulo(10)

triangulo1 = Triangulo(5,2)


figuras = [rectangulo1, triangulo1, circulo1]

for figura in figuras:
    figura.dibujar()
    print(figura.calcular_area())
    print(type(figura))
    print(isinstance(figura, Figura))