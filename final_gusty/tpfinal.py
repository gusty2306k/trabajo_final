import tkinter as tk
import requests

# Define la clase Pokemon.
class Pokemon:
    def __init__(self, nombre, tipo, habilidades, estadisticas):
        self.nombre = nombre
        self.tipo = tipo
        self.habilidades = habilidades
        self.estadisticas = estadisticas

#Funcion para obtener información de la API de Pokémon
def obtener_informacion():
    pokemon_id = entrada_id.get()  # Obtiene el ID del Pokémon ingresado en la entrada.
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)

    if response.status_code == 200:  # Verificar si la solicitud fue exitosa (código 200)
        data = response.json()  # Convertir la respuesta a formato JSON

        # Intentar obtener datos específicos de la respuesta JSON
        try:
            nombre = data['name']  # Nombre del Pokémon
            tipo = data['types'][0]['type']['name']  # Tipo del Pokémon
            habilidades = [habilidad['ability']['name'] for habilidad in data['abilities']]  # Lista de habilidades
            estadisticas = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}  # Estadísticas del Pokémon

            # Muestra la información obtenida en etiquetas.
            etiqueta_nombre.config(text=f"Nombre: {nombre}")
            etiqueta_tipo.config(text=f"Tipo: {tipo}")
            etiqueta_habilidades.config(text=f"Habilidades: {', '.join(habilidades)}")
            etiqueta_estadisticas.config(text="Estadísticas:")

            for stat, value in estadisticas.items():
                etiqueta = tk.Label(ventana, text=f"{stat}: {value}")
                etiqueta.pack()
        except KeyError:
            etiqueta_nombre.config(text="¡Pokémon no encontrado o estructura de datos incorrecta!")
    else:
        etiqueta_nombre.config(text="¡Error al obtener información del Pokémon!")

#ventana principal.
ventana = tk.Tk()
ventana.title("Obtener Información de Pokémon")
ventana.geometry("400x400")

# Crea una etiqueta y una entrada para el ID del Pokémon.
etiqueta_id = tk.Label(ventana, text="ID del Pokémon:")
etiqueta_id.pack()

entrada_id = tk.Entry(ventana)
entrada_id.pack()

#botón para obtener información, al hacer clic ejecuta la función obtener_informacion.
boton_obtener = tk.Button(ventana, text="Obtener información", command=obtener_informacion)
boton_obtener.pack()

#etiqueta para mostrar la información del Pokémon.
etiqueta_nombre = tk.Label(ventana, text="")
etiqueta_nombre.pack()

etiqueta_tipo = tk.Label(ventana, text="")
etiqueta_tipo.pack()

etiqueta_habilidades = tk.Label(ventana, text="")
etiqueta_habilidades.pack()

etiqueta_estadisticas = tk.Label(ventana, text="")
etiqueta_estadisticas.pack()

# Ejecuta el bucle.
ventana.mainloop()
