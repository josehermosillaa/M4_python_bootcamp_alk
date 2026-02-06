import requests
import json

peliculas = []
url = 'https://ghibliapi.vercel.app/films/'
# url = 'https://www.google.com/'
response = requests.get(url)
print(response)

# print(response.text)
#codigo 200, exitoso
#codigo 404, no encontrado

datos = response.json() #con esto python entiende que es una lista de diccionarios (ya que viene en formato json)

# print(len(datos))

for pelicula in datos :
    peliculas.append({
        "titulo":pelicula["title"],
        "titulo_original": pelicula["original_title"],
        "imagen":pelicula["image"],
        "director":pelicula["director"],
        "descriptcion":pelicula["description"]
    }
    )

with open('datos_peliculas_gibli.json','w', encoding='utf-8') as archivo:
    json.dump(peliculas,archivo, indent=4)