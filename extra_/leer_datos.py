import json

with open("datos_peliculas_gibli.json",'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)
#datos ahora seria una lista de diccionarios
#nosotros con este formato, nos es dificil poder manejarlo directamente como un diciconario
for usuario in datos:
    print(usuario["titulo_original"])