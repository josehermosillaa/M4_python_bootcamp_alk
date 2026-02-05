"""Implementá un programa en Python que:
Solicite al usuario el nombre de un archivo
Abra el archivo en modo lectura ("r")
Obtenga y muestre:
Nombre del archivo (.name)
Modo de apertura (.mode)
Estado de cierre (.closed)
Tamaño en bytes usando os.stat()
Lea el contenido:
Si el archivo pesa menos de 500 bytes → leé todo el contenido con read()
Si pesa más de 500 bytes → leé línea por línea con readline()
Asegurate de cerrar el archivo y mostrar que fue cerrado correctamente
Usá try/except para manejar errores si el archivo no existe
"""
"""
1. Importar el módulo os
2. Solicitar al usuario la ruta o nombre del archivo
3. Intentar abrir el archivo en modo "r" usando try/except
4. Mostrar atributos básicos del archivo (name, mode, closed)
5. Obtener el tamaño usando os.stat().st_size
Según el tamaño:
Si es pequeño → leer todo con read()
Si es grande → usar readline() en un bucle
Cerrar el archivo
Confirmar que el archivo está cerrado (.closed)
En caso de error (archivo no encontrado), mostrar un mensaje claro al usuario
"""
import os
print("El archivo a ser leido debe encontrarse en la carpeta de este script")
ruta = input("Ingrese el nombre del archivo con su extension(.txt,.log,.json, etc): ")

try:
    archivo = open(ruta, 'r')
    print("Nombre del archivo: ",archivo.name)
    print("Modo de apertura del archivo: ",archivo.mode)
    print("Se ecuentra cerrado?",archivo.closed)
    tamannio = os.stat(ruta).st_size
    print("Tamaño del archivo en bytes:", tamannio)
    if tamannio < 500:
        print("El archivo es pequeño, usando el metodo read para leer ...." )
        print(archivo.read())
    elif tamannio >= 500:
        print("El archivo es grande, usando el metodo readline para leer ...." )
        while True:
            linea = archivo.readline()

            if not linea: #no existe la linea, esdecir archivo.readline() == None
                # archivo.close()
                break
            
            print(linea)
            

except FileNotFoundError:
    print(f"archivo no encontrado, revise su ruta")
except Exception as e:
    print("Se detecto otro error:" , e)

else:
    print("Intentamos cerrar el archivo")

    if not archivo.closed:
        archivo.close()
        print("El archivo se cerro correctamente")

finally:
    print("Saliendo del script...")