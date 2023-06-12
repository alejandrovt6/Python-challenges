"""
This program implement an HTTP call to a Poke API and show Pokemon, name and type.
"""

# Libraries
import requests, os, sys
from PIL import Image, ImageTk
import tkinter as tk

# API
response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')

# Program
def poke_name(num):
    if response.status_code == 200:
        data = response.json()
        result = data.get('results',[])
        if result:
            name = result[num]['name'].capitalize()
            # print("Your Pokemon is: " + name)
            return name

def poke_type(num):
    if response.status_code == 200:
        data = response.json()
        result = data.get('results',[])
        if result:
            pokemon_url = result[num]['url']
            pokemon_data = requests.get(pokemon_url).json()
            types = []
            for t in pokemon_data['types']:
                types.append(t['type']['name'].capitalize())
            type_str = ', '.join(types)
            return type_str

def get_pokemon_image_url(num):
    if response.status_code == 200:
        data = response.json()
        result = data.get('results', [])
        if result:
            pokemon_url = result[num]['url']
            pokemon_data = requests.get(pokemon_url).json()
            image_url = pokemon_data['sprites']['front_default']
            return image_url

def search_pokemon():
    try:
        num = int(entry.get())
        # Subtract 1 from num to account for 0-based indexing
        name = poke_name(num - 1) 
        if name:
            type_str = poke_type(num - 1)
            image_url = get_pokemon_image_url(num - 1)
            if image_url:
                display_pokemon_image(name, image_url)
        else:
            print("Pokemon not found.")
    except ValueError:
        print("ERROR: Type a number.")
        
def display_pokemon_image(name, image_url):
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        # Create the pokemon folder if it doesn't exist and save it
        if not os.path.exists('pokemon'):
            os.makedirs('pokemon')
        image_path = os.path.join('pokemon', f'{name}.png')
        with open(image_path, 'wb') as out_file:
            out_file.write(response.content)
        image = Image.open(image_path)
        # Convert the image to a Tkinter-compatible format
        tk_image = ImageTk.PhotoImage(image)
        
        type_str=""
        
        # Get the pokemon type
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name.lower()}')
        if response.status_code == 200:
            pokemon_data = response.json()
            types = []
            for t in pokemon_data['types']:
                types.append(t['type']['name'].capitalize())
            type_str = ', '.join(types)
        
        label_name = tk.Label(window, text=name.capitalize())
        label_name.pack()
        
        label_type = tk.Label(window, text=f"Type(s): {type_str}")
        label_type.pack()

        label_image = tk.Label(window, image=tk_image)
        label_image.image = tk_image  
        label_image.pack()

        window.mainloop()

# GUI
window = tk.Tk()
window.title("Pokedex")

window.iconbitmap('icons/pokeball.ico')

window.geometry("400x400")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width - window.winfo_screenmmwidth()) / 2)
y = int((screen_height - window.winfo_screenmmheight()) / 2)

window.geometry("+{}+{}".format(x, y))

label = tk.Label(window, text="Enter the number of the Pokemon you want to search for:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Search", command=search_pokemon)
button.pack()

window.mainloop()
