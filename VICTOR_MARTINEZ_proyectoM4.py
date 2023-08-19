import os
import json
import requests

def buscar_pokemon(nombre):#funcion para buscar el pokemon 
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"#definimos el api
    respuesta = requests.get(url)

    if respuesta.status_code == 404:#validamos respuestas 
        return None
    elif respuesta.status_code == 200:
        datos_pokemon = respuesta.json()
        return datos_pokemon
    else:
        raise Exception(f"Error al buscar el Pokémon: {respuesta.status_code}")

def guardar_pokemon_en_json(pokemon):#guardamos el pokemon
    nombre = pokemon['name']
    carpeta = "pokedex"

    if not os.path.exists(carpeta):
        os.mkdir(carpeta)

    with open(os.path.join(carpeta, f"{nombre}.json"), 'w') as archivo:
        json.dump(pokemon, archivo, indent=4)

def mostrar_info_pokemon(pokemon):#en esta parte se muestra la informacion del pokemon  
    print(f"Nombre: {pokemon['name'].capitalize()}")
    print(f"Peso: {pokemon['weight']}")
    print(f"Tamaño: {pokemon['height']}")

    print("Habilidades:")#aqui se imprimen las habilidades 
    for habilidad in pokemon['abilities']:
        print(f"- {habilidad['ability']['name']}")

    print("Tipos:")#aqui sus tipos 
    for tipo in pokemon['types']:
        print(f"- {tipo['type']['name']}")

    print("Movimientos:")#aqui los primeros 10 movimientos 
    for movimiento in pokemon['moves'][:10]:  # Mostrar los primeros 10 movimientos
        print(f"- {movimiento['move']['name']}")

    print("Imagen:")#este es el apartado de la imagen 
    imagen_url = pokemon['sprites']['front_default']
    print(imagen_url)

if __name__ == "__main__":
    nombre_pokemon = input("Introduce el nombre de un Pokémon: ")#ingreso de datos
    pokemon = buscar_pokemon(nombre_pokemon)

    if pokemon is None:#si el pokemon no se encuentra en la api 
        print(f"No se encontró el Pokémon {nombre_pokemon}.")
    else:
        mostrar_info_pokemon(pokemon)
        guardar_pokemon_en_json(pokemon)