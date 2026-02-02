"""
¿En qué consistirá la Demo?
Vas a crear una jerarquía de clases (Usuario,
 Administrador, Cliente) y usar isinstance() 
para aplicar acciones según el tipo de objeto

🔹 Clases involucradas:
Clase base Usuario:

Método saludar() común a todos

Subclases:

Administrador: método acceder_panel()

Cliente: método realizar_compra()

🔹 Qué se debe probar:

Crear una lista de objetos mezclados (Cliente, Administrador, Usuario)
Iterar sobre la lista
Usar isinstance() para ejecutar acciones según el tipo:
Si es Administrador → llamar acceder_panel()
Si es Cliente → llamar realizar_compra()
Si es Usuario → llamar solo saludar()

"""

class Usuario:
    def __init__(self,nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola bienvenido {self.nombre}")

class Administrador(Usuario):
    def __init__(self, nombre):
        super().__init__(nombre)

    def acceder_panel(self):
        print("Administrador accedido correctamente")
        return True

class Soporte(Usuario):
    print("Mayor  poder que el usuario y menor que el administrador")    

class Cliente(Usuario):
    def __init__(self, nombre):
        super().__init__(nombre)

    def realizar_compra(self):
        print(f" Compra realizada, que lo disfrutes {self.nombre}")
        return True
    

usuario = Usuario("Juan")
adminstrador = Administrador("Roberto")
cliente = Cliente("Pedrito")

personas = [ usuario, adminstrador, cliente]

for persona in personas:

    if isinstance(persona, Cliente):
        persona.realizar_compra()
    elif isinstance(persona, Administrador):
        persona.acceder_panel()
    elif isinstance(persona, Usuario):
        persona.saludar()