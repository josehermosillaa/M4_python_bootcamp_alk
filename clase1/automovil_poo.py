"""Ejemplo de clases y objetos"""

class Automovil:
    def __init__(self, color,marca,modelo,velocidad = 0):
        self.color  = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    #metodos se definen como las acciones de los objetos

    def encender_auto(self):
        if self.velocidad > 0:
            print("El auto ya se encuentra encendido")
        else:
            print("Se ha encendido el auto correctamente")
    
    #tanto para acelerar como para frenar vamos a aumentar o disminuir en 5 km/h
    def acelerar(self):
        print(f"Velocidad antes de acelerar {self.velocidad} km/h")
        self.velocidad += 5
        print(f"Velocidad despues de acelerar {self.velocidad} km/h")

    def frenar(self):
        
        print(f"Velocidad antes de frenar {self.velocidad} km/h")
        if self.velocidad != 0:
            self.velocidad -= 5
            if self.velocidad >0:
                self.velocidad = 0
                print(f"Velocidad despues de frenar {self.velocidad} km/h")
        else:
            print("El auto ya se encontraba detenido")
    
        
changan = Automovil("rojo","changan","CS-15") #primer objeto

print(changan.color)

# changan.encender_auto()
changan.acelerar()
changan.frenar()
changan.frenar()


mg = Automovil("gris","MG", "ZX", 3) #un segundo objeto
#diferenciamos los objetos por que poseen atrributos distintos