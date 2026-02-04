#Metodo r
#1 usamos open para abrir el archivo
archivo = open('prueba.txt', 'r')
#Sie el archivo a leer con el modo r no esta en la carpeta, se lanza la excepcion FileNotFoundError
print(archivo.read()) # .read() devuelve el texto del archivo

print("Nomnbre: ", archivo.name )
print("Modo: ", archivo.mode )
print("esta cerrado?: ", archivo.closed)

archivo.close()
print("esta cerrado?: ", archivo.closed)
