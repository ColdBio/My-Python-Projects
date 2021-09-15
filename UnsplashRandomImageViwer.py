import tkinter as tk
from tkinter import ttk
import json
import requests        
from PIL import Image, ImageTk
import io
import urllib.request
from io import BytesIO
import string


window = tk.Tk()
window.title("Unsplash Random Image Viewer")

# You can change the number of images returned by altering the 'count' to a desired number
url = "https://api.unsplash.com/photos/random?client_id={Replace with your own API key}&count=10"
url = requests.get(url)
data = json.loads(url.text)

image_list = []
desc_list = []
username_list = []
likes_list = []
downloads_list = []
views_list = []


for each in data:
    image_list.append(each["urls"]["regular"])

for each in data:
    desc_list.append(each["alt_description"])

for each in data:
    username_list.append(each["user"]["username"])

for each in data:
    likes_list.append(each["likes"])

for each in data:
    downloads_list.append(each["downloads"])

for each in data:
    views_list.append(each["views"])

def get_url_image(some_input):
    image = urllib.request.urlopen(some_input)
    img_data = image.read()
    im = Image.open(BytesIO(img_data))
    width, height = im.width, im.height
    im = im.resize((int(width / 5), int(height / 5)))
    image = ImageTk.PhotoImage(im)
    return image

images = []

for each in image_list:
    images.append(get_url_image(each))

img_iter = iter(images)
desc_iter = iter(desc_list)
username_iter = iter(username_list)
likes_iter = iter(likes_list)
downlaods_iter = iter(downloads_list)
views_iter = iter(views_list)

image = tk.Label(image=next(img_iter))
alt_desc = tk.Label(text=next(desc_iter))

username = tk.Label(text="Username: " + next(username_iter))
likes = tk.Label(text=f"Likes: {next(likes_iter)}")
downalods = tk.Label(text=f"Downalods: {next(downlaods_iter)}")
views = tk.Label(text=f"Views: {next(views_iter)}")

image.grid(row=1, column=1)
alt_desc.grid(row=2, column=1)

username.grid(row=3, column=1)
likes.grid(row=4, column=1)
downalods.grid(row=5, column=1)
views.grid(row=6, column=1)


def refresh():
    try:
        image['image'] = next(img_iter)
        alt_desc['text'] = next(desc_iter)
        window.after(2500, refresh)
    except StopIteration:
        pass


window.after(2500, refresh)
window.eval('tk::PlaceWindow . center')
window.mainloop()
