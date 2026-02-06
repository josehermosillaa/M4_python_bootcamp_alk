import json

datos = [
    {
    "nombre":"jose",
    "edad": 34,
    "direcicon": "Av siempre viva 766, SpringField"
},
]

########
"""
lo ideal seria crear una funcion que solicite al usuario los datos de entrada y los almacene en la lista datos

"""
#######
#ejemplo
datos.append({
    "nombre":"pedrito",
    "edad": 18,
    "direcicon": "otro, SpringField"
})

datos.append({
    "nombre":"ana",
    "edad": 24,
    "direcicon": "otro, SpringField"
})

with open('datos_usuarios.json','w', encoding='utf-8') as archivo:
    json.dump(datos,archivo, indent=4)