import tkinter
from PIL import Image, ImageTk
from urllib.request import urlopen
import requests
from tkinter import messagebox


def get_data():
    for delete_widget in list_of_delete:
        delete_widget.destroy()

    pokemon_name= pokemon_name_entry.get()
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_name.lower()
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pokemon_name = data["name"]
        pokemon_base_experience = data["base_experience"]
        pokemon_height = data["height"]
        pokemon_weight = data["weight"]
        pokemon_picture = data["sprites"]["other"]["home"]["front_default"]
        pokemon_ability_list = []
        ability_list_len = len(data["abilities"])
        for i in range(0, ability_list_len):
            pokemon_ability = data["abilities"][i]["ability"]["name"]
            pokemon_ability_list.append(pokemon_ability)

        pokemon_stats_dic = {}
        stats_len = len(data["stats"])
        for y in range(0, stats_len):
            stats_name = data["stats"][y]["stat"]["name"]
            pokemon_stats_dic[f"{stats_name}"] = data["stats"][y]["base_stat"]

        pokemon_types_list = []
        types_list_len = len(data["types"])
        for x in range(0, types_list_len):
            pokemon_type = data["types"][x]["type"]["name"]
            pokemon_types_list.append(pokemon_type)

        pokemon_image_url = urlopen(pokemon_picture)
        raw_data = pokemon_image_url.read()
        pokemon_image_url.close()
        
        pokemon_photo = ImageTk.PhotoImage(data=raw_data)
        photo_label= tkinter.Label(image=pokemon_photo, width=500 , height= 500 , bg=BG, pady=45)
        photo_label.image = pokemon_photo
        photo_label.pack(side=tkinter.LEFT)
        list_of_delete.append(photo_label)

        pokemon_name_label= tkinter.Label(text=pokemon_name.capitalize(), font=NAME_FONT, fg="dark olive green", pady=5, bg=BG)
        pokemon_name_label.pack()
        list_of_delete.append(pokemon_name_label)

        pokemon_weight_label= tkinter.Label(text="Weighs: " + str(pokemon_weight), font=TEXT_FONT, bg=BG)
        pokemon_weight_label.pack()
        list_of_delete.append(pokemon_weight_label)

        pokemon_height_label= tkinter.Label(text="Height: " + str(pokemon_height), font=TEXT_FONT, bg=BG)
        pokemon_height_label.pack()
        list_of_delete.append(pokemon_height_label)

        pokemon_base_experience_label= tkinter.Label(text="Base Experience: " + str(pokemon_base_experience), font=TEXT_FONT, bg=BG)
        pokemon_base_experience_label.pack()
        list_of_delete.append(pokemon_base_experience_label)


        pokemon_stats_label = tkinter.Label(text="Stats:", font=TITLE_FONT, bg=BG , pady=5)
        pokemon_stats_label.pack()
        list_of_delete.append(pokemon_stats_label)

        for x in pokemon_stats_dic:
            pokemon_stats = tkinter.Label(text=x.capitalize() + " : " + str(pokemon_stats_dic[x]),font=ARTICLE_FONT, bg=BG)
            pokemon_stats.pack()
            list_of_delete.append(pokemon_stats)

        pokemon_ability_label = tkinter.Label(text="Abilities: ", font=TITLE_FONT, bg=BG, pady=5)
        pokemon_ability_label.pack()
        list_of_delete.append(pokemon_ability_label)

        for ability in pokemon_ability_list:
            pokemon_ability = tkinter.Label(text=str(pokemon_ability_list.index(ability) + 1)+ "." + ability.capitalize(), font=ARTICLE_FONT, bg=BG)
            pokemon_ability.pack()
            list_of_delete.append(pokemon_ability)

        pokemon_type_label = tkinter.Label(text="Types:", font=TITLE_FONT, bg=BG, pady=5)
        pokemon_type_label.pack()
        list_of_delete.append(pokemon_type_label)

        for type in pokemon_types_list:
            poke_type = tkinter.Label(text=type.capitalize(),font=ARTICLE_FONT, bg=BG)
            poke_type.pack()
            list_of_delete.append(poke_type)

    else:
        messagebox.showinfo("Infromation", "Pokemon isimini yanlış girdiniz.")


window = tkinter.Tk()
BG = "burlywood"
NAME_FONT = ("Arial", 25, "bold", "underline")
TEXT_FONT = ("Arial", 13, "italic")
TITLE_FONT = ("Arial", 13, "italic", "underline", "bold")
ARTICLE_FONT = ("Arial", 11, "italic")

window.title("Pokemon Info Giver")
window.config(pady=10, padx=50, bg=BG)

name_label = tkinter.Label(text="POKEMON INFO GIVER", font=("Arial", 28, "bold"), fg="DarkBlue", bg=BG)
name_label.config(pady=25)
name_label.pack()

wanted_label = tkinter.Label(text="Enter Pokemon Name", font=("Arial", 12), bg=BG)
wanted_label.pack()

pokemon_name_entry = tkinter.Entry(width=30)
pokemon_name_entry.pack()

search_button = tkinter.Button(text="Search", command=get_data)
search_button.pack()

photo_label = tkinter.Label()
pokemon_name_label = tkinter.Label()
pokemon_weight_label = tkinter.Label()
pokemon_height_label = tkinter.Label()
pokemon_base_experience_label = tkinter.Label()
pokemon_stats_label = tkinter.Label()
pokemon_ability_label = tkinter.Label()
pokemon_type_label = tkinter.Label()
list_of_delete = []



window.mainloop()

