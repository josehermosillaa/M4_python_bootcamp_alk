# import os

# os.stat()



#2 readline
archivo = open('accesos.log', 'r')

usuarios = [] #lista vacia

lineas = archivo.readlines() #me genera una lista de cada linea

for linea in lineas:
    iterable = linea.strip().split(';')
    usuarios.append(iterable[1])


#mostrar los usuarios unicos de la plataforma

usuarios = set(usuarios)

print("Usuarios unicos: ", usuarios)
