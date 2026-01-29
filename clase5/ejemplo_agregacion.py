#una relacion de agregacion podria ser Material y Pelota    

class Material():
    #metodo de inicializacion de atributos de una clase
    #aquio se definen los atributos necesarios para instanciar un objeto de la clase
    def __init__(self, nombre:str, duracion:str, textura:str): #esta notacion no quiere decir que en nombre solo pueda ingresar texto
        #dado la naturaleza de Python podriamos ingresar un numero o un bool
        #es masa para notacion de dato que una regla
        
        self.nombre = nombre
        self.duracion = duracion
        self.textura = textura

class Pelota():
    def __init__(self, tamanio:int, color:str, material:Material):
        self.tamanio = tamanio
        self.color = color
        #la pelota tiene un material
        self.material = material


material = Material("Plastico", "Corta", "Lisa")
pelota = Pelota(16, "Amarillo", material)

print(type(pelota.material))

print(pelota.material.nombre)