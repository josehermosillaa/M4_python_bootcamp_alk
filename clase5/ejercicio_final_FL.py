class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def moverse(self):
        print(f" El vehiculo, marca {self.marca}, modelo {self.modelo}. se esta moviendo")


class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas
    def moverse(self):
        print(f" El vihiculo, marca {self.marca}, modelo {self.modelo}, de {self.puertas} puertas. se esta moviendo, conduciendo por la carretera")

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo, material):
        super().__init__(marca, modelo)
        self.tipo = tipo
        self.material = material
    def moverse(self):
        print(f" El vihiculo, marca {self.marca}, modelo {self.modelo}, biciclet del tipo {self.tipo}, construida en {self.material}, se esta moviendo, va pedaleando rajada por carretera")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindros):
        super().__init__(marca, modelo)
        self.cilindros = cilindros
    def moverse(self):
        print(f" El vihiculo, marca {self.marca}, modelo {self.modelo}, con sus {self.cilindros} cilindros, va conduciendo por carretera")



#AUTOS
auto1 = Auto("Toyota", "Corolla", 4)
auto2 = Auto("Nissan", "Versa", 4)
auto3 = Auto("Chevrolet", "Spark", 5)
auto4 = Auto("Hyundai", "Accent", 4)
auto5 = Auto("Kia", "Rio", 4)
auto6 = Auto("Ford", "Focus", 4)
#BICIS
bici1 = Bicicleta("Trek", "X100", "Montaña", "Aluminio")
bici2 = Bicicleta("Giant", "Speed", "Ruta", "Carbono")
bici3 = Bicicleta("Oxford", "Urban", "Urbana", "Acero")
bici4 = Bicicleta("Scott", "Pro", "Montaña", "Carbono")
bici5 = Bicicleta("Bianchi", "Elite", "Ruta", "Aluminio")
bici6 = Bicicleta("Specialized", "Rock", "Montaña", "Acero")
#MOTOS
moto1 = Motocicleta("Yamaha", "R3", 2)
moto2 = Motocicleta("Honda", "CBR", 2)
moto3 = Motocicleta("Suzuki", "GSX", 4)
moto4 = Motocicleta("Kawasaki", "Ninja", 2)
moto5 = Motocicleta("BMW", "S1000", 4)
moto6 = Motocicleta("Ducati", "Monster", 2)



auto1.moverse()
auto2.moverse()
auto3.moverse()
auto4.moverse()
auto5.moverse()
auto6.moverse()

bici1.moverse()
bici2.moverse()
bici3.moverse()
bici4.moverse()
bici5.moverse()
bici6.moverse()

moto1.moverse()
moto2.moverse()
moto3.moverse()
moto4.moverse()
moto5.moverse()
moto6.moverse()