import json
import requests
import tkinter as tk
from PIL import Image, ImageTk
import io
import urllib.request
from io import BytesIO

url = requests.get("https://api.nasa.gov/planetary/apod?api_key={replace with your own key here}}")
data = json.loads(url.text)

def get_url_image():
    image = urllib.request.urlopen(data["hdurl"])
    img_data = image.read()
    return img_data

def GUI():
    window = tk.Tk()

    # Labels
    title = tk.Label(text = data["title"])
    date = tk.Label(text = data["date"])
    explanation = tk.Label(text = data["explanation"], wraplength=1000, justify="center")


    # Image handling
    img_data = get_url_image()

    im = Image.open(BytesIO(img_data))
    width, height = im.width, im.height

    im = im.resize((int(width / 5), int(height / 5)))
    image = ImageTk.PhotoImage(im)

    apod_image = tk.Label(image=image)
    
    
    
    title.pack()
    date.pack()
    apod_image.pack()
    explanation.pack()
    window.title("🔭 Nasa Astronomy Picture of the Day 🪐")
    window.mainloop()

GUI()

"""
References:-

1. https://api.nasa.gov
   API data provided by NASA 

2. https://stackoverflow.com/questions/44171567/how-to-add-a-url-image-to-tkinter-in-python-2-7-using-only-the-standard-python-l
   This stackoverflow provided code that takes an image from a url and displays it

"""
