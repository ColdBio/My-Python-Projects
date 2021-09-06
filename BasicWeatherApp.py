import json
from tkinter.constants import S
import requests
import tkinter as tk
from tkinter import ttk
import urllib.request
from io import BytesIO
import io
from PIL import Image, ImageTk

def weather_api():

    url = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q=Paris&units=metric&appid=3d128e7aa2598d339e63306ea159e691")
    data = json.loads(url.text)

    city_name = data["name"]
    temp = data["main"]["temp"]
    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    feels_like = data["main"]["feels_like"]

    icon = data["weather"][0]["icon"]
    description = data["weather"][0]["description"]

    icon_url = (f"http://openweathermap.org/img/wn/{icon}@2x.png")
    
    country_initials = data["sys"]["country"]
    print(country_initials)


    return city_name, temp, temp_min, temp_max, pressure, humidity, feels_like, icon_url, description, country_initials


def image_extractor(url):
    image = urllib.request.urlopen(f"{url}")
    image_data = image.read()
    return image_data


def GUI():

    # Assigning API data to their respective variables
    city_name, temp, temp_min, temp_max, pressure, humidity, feels_like, icon_url, description, country_initials = weather_api()

    window = tk.Tk()
    window.title("Simple Weather")


    # Creating Labels
    city_name_label = tk.Label(text=f"{city_name} {country_initials}")
    city_name_label.config(font=("Calibri", 24))

    temp_label = tk.Label(text=f"{round(temp, 1)}°C")
    temp_label.config(font=("Calibri", 34))

    description_label = tk.Label(text=f"{description.capitalize()}")
    description_label.config(font=("Calibri", 14))

    temp_min_max_label = tk.Label(text=f"min: {round(temp_min, 1)}°C      max: {round(temp_max, 1)}°C")
    temp_min_max_label.config(font=("Calibri", 14))


    # Dealinng with the Image icon
    image_data = image_extractor(icon_url)
    im_byte = Image.open(BytesIO(image_data))
    width, height = im_byte.width, im_byte.height
    image_icon = ImageTk.PhotoImage(im_byte)
    image_label = tk.Label(image=image_icon)


    # Placing UI elements in the desired order
    city_name_label.grid(row=1, column=2)
    image_label.grid(row=2, column=2)
    temp_label.grid(row=3, column=2)
    description_label.grid(row=4, column=2)
    temp_min_max_label.grid(row=5, column=2)

    window.mainloop()

GUI()


