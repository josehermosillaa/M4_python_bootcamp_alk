"""Modelá una clase Libro que contenga atributos públicos y privados. 
Utilizá getters y setters para proteger el precio,
y diseñá un método para realizar ventas que actualicen el stock.
Paso a paso: ⚙️
1. Definí los atributos: titulo, autor, stock (públicos) y __precio (privado)
2. Implementá get_precio() y set_precio() validando que sea un valor positivo
3. Agregá un método vender(unidades) que descuente del stock si hay suficiente
4. Creá el método mostrar_info() para imprimir todos los datos del libro
5. Probá con varios objetos


"""

class Libro:

    def __init__(self, titulo, autor, stock, precio):
        self.titulo = titulo
        self.autor = autor
        self.stock = stock
        self.__precio = precio #privada
    


    #vimos las funciones getter y setter #funciones accesadoras

    def get_precio(self):
        return self.__precio
    ##si quisieramos usar esta funcion para validar el precio en el __init__ deberiamos
    ##usar un raise para lanzar un valueerror y asi no permitir la creacion de un Libro
    ## sin el atributo precio
    ##ver ejercicio control_precio.py

    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Precio no modificado, Ingrese un valor valido")

    def vender_unidades(self, cantidad = 1):
        if self.stock >= cantidad : #stock debe tener las mismas o mas unidades que la cantidad
            print(f"se vendieron {cantidad} de {self.titulo}")
            self.stock = self.stock - cantidad
            print(f"nuevo stock {self.stock}")
        else:
            print(f"cantidad fuera de stock, stock actual {self.stock}")

    def mostrar_info(self):
        print(f"Titulo: {self.titulo}|Autor: {self.autor} |stock: {self.stock} | Precio: {self.__precio} ")

libro1 = Libro("Cien años de soledad","Gabriel Garcia Marquez", 5,12000)
libro2 = Libro("Clean Code","Robert C. Martin", 3, 40000)


libro1.mostrar_info()
print(libro1.get_precio())
libro2.mostrar_info()
print(libro2.get_precio())

libro1.set_precio(8000)
print(libro1.get_precio())
libro1.set_precio(-111000)
print(libro1.get_precio())

libro2.vender_unidades(10)
libro2.vender_unidades(2)
libro2.mostrar_info()
