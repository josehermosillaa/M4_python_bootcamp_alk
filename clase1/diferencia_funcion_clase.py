###Funciones
def crear_cliente(nombre, edad):
    return {"nombre": nombre, "edad":edad}

def saludar(cliente):
    print(f"Hola {cliente["nombre"]}")

cliente = crear_cliente("Ana", 30)
saludar(cliente)

###si lo hacemos con clase o POO

class Cliente:
    #esta funcion es la que se aplica al crear un objeto de la clase
    #se definen a partir de ellla los atributos de entrada para la misma

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #hasta este punto estariamos cumpliendo con lo mismo que hace la funcion crear_cleinte
    #toda funcion despues de la funcion __init__ se conoce como metodo y representa las acciones de la clase
    #esto representa la funciona saludar anterior
    def saludar(self):
        print(f"Hola {self.nombre}")

    def sumar_edad(self):
        self.edad = self.edad + 1
        print(f"la nueva edad de {self.nombre} es: {self.edad}")

 
cliente = Cliente("Juan", 19) #aqui se crea un objeto de la clase con atributos nombre =juan yu edad = 19 
#y ademas tiene el metodo o accion de la clase que es saludar

cliente.saludar()
print(cliente.edad)
cliente.sumar_edad()
