
"""
Usar open() en modo "r" para abrir un archivo llamado "prueba.txt"
Leer el contenido usando read()
Imprimir el contenido en consola
Cerrar el archivo usando close()

🔹 Observaciones importantes:

Si el archivo no existe, Python lanzará un FileNotFoundError

Verificar si el archivo realmente se cerró con archivo.closed

"""
#Metodo r
#1 usamos open para abrir el archivo
archivo = open('prueba.txt', 'r')
#Sie el archivo a leer con el modo r no esta en la carpeta, se lanza la excepcion FileNotFoundError
print(archivo.read()) # .read() devuelve el texto del archivo
archivo.close()

# #2 Metodo  W

# archivo = open('pruebaw.txt', 'w')
# # print(archivo.read()) #cuando abrimos el archivo en el modo w, no se puede leer es el modo escritura
# archivo.write("Soy otro texto")
# archivo.close() 


# # #si abrimos un archivo que no existe con el metodo w, se crea automaticamente
# # for doc in range(5):
# #     archivo = open(rf'pruebaw{doc}.txt', 'w')
# #     # print(archivo.read()) #cuando abrimos el archivo en el modo w, no se puede leer es el modo escritura
# #     archivo.write(rf"Soy otro texto {doc}")
# #     archivo.close()


# #3 Metodo a
# #si intentamos abrir un archivo que no existe en el modo a?
# archivo = open('pruebaa.txt', 'a')
# # print(archivo.read()) #cuando abrimos el archivo en el modo w, no se puede leer es el modo escritura
# archivo.write("Soy otro texto\n")
# archivo.close() 

# #para escribir 50 lineas

# for i in range(50):
#     archivo = open('pruebaw.txt', 'a')
#     # print(archivo.read()) #cuando abrimos el archivo en el modo w, no se puede leer es el modo escritura
#     archivo.write("Soy otro texto\n")
#     archivo.close() 