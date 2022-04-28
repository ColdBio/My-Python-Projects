import tkinter as tk
from tkinter import ttk
from pytube import YouTube
from tqdm import tqdm
from tkinter import messagebox
from PIL import Image, ImageTk
import io
import urllib.request
from io import BytesIO

"""
Credit to Pytube for providing a lightweight, dependency-free Python library (and command-line utility) for downloading YouTube Videos.
Github: https://github.com/pytube/pytube
Documentation: https://pytube.io/en/latest/

"""


all_res = ["240p", "360p", "480p", "720p", "1080p", "1440p", "2160p"]

def get_url_image(data):
    image = urllib.request.urlopen(data)
    img_data = image.read()
    return img_data


class Python_Video_Downloader:




    def GUI():
        window = tk.Tk()
        window.title("🐍 Python Youtube Downloader ▶️")

        link_label = tk.Label(text="Video URL: ")
        link_entry = tk.Entry(text="", width=40)
        download_path_label = tk.Label(text="Download Path: ")
        download_path = tk.Entry(text="", width=40)
        video_title = tk.Label(text="Video Title: ")
        select_res = ttk.Combobox(window, values=all_res)
        select_res.current(0)

        def find_video():
            user_link = link_entry.get()
            try:
                yt = YouTube(user_link)
                print(yt.title)
                print(yt.thumbnail_url)
                yt_thumbnail = get_url_image(yt.thumbnail_url)

                im = Image.open(BytesIO(yt_thumbnail))
                width, height = im.width, im.height

                im = im.resize((int(width / 5), int(height / 5)))
                image = ImageTk.PhotoImage(im)
                print(image)


                video_title['text'] = "Video Title: " + yt.title       
                print(select_res.get())       

            except Exception as e:
                print(e)
                messagebox.showerror("Error", f"Invalid URL link")

        def download_selected_video():
            print("Starting...")
            yt = YouTube(f"{link_entry.get()}")
            stream_list = yt.streams.filter(file_extension='mp4', res=f"{select_res.get()}")
            print(stream_list)
            for each in stream_list:
                try:
                    print("Downloading...")
                    each.download(output_path=f"{download_path.get()}")
                    print("Complete")
                except Exception as e:
                    print(f"[!] Error {e}")
            print("Complete")

        find_btn = tk.Button(text="Find Video", command=find_video)
        download_btn = tk.Button(text=" Download Video", command=download_selected_video)


        link_label.grid(row=1, column=1)
        link_entry.grid(row=1, column=2)
        find_btn.grid(row=1, column=3)
        video_title.grid(row=2, column=2)
        select_res.grid(row=2, column=3)
        download_path_label.grid(row=4, column=1)
        download_path.grid(row=4, column=2)
        download_btn.grid(row=4, column=3)
        window.mainloop()


Python_Video_Downloader.GUI()
