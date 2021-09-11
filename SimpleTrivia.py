# The code below fetches data from an api that provides trivia related information and displays it in a simple GUI. 
# The api can be viewed from here:- https://opentdb.com/api_config.php

import json
import requests
import tkinter as tk
import html

# Accessing API data
response = requests.get("https://opentdb.com/api.php?amount=1")
data = json.loads(response.text)

# Making sure to only deal with the needed data
for each in data["results"]:
    category = html.unescape(each["category"])
    question = html.unescape(each["question"])
    answer = html.unescape(each["correct_answer"])
    difficulty = html.unescape(each["difficulty"])

# GUI
window = tk.Tk()
window.title("✅ Simple Trivia ❌")

labelC = tk.Label(text=f"Category: {category}")
labelQ = tk.Label(text=f"Question: {question}")
labelA = tk.Label(text=f"Answer: {answer}")

# Consider adding a refresh button that reloads the window again so a new question can be posed
new_question = tk.Button(window, text="New Question")

# Based on difficulty a visual cue is displayed
if difficulty == "hard":
    labelD = tk.Label(text=f"Difficulty: {difficulty}", fg="red")
elif difficulty == "medium":
    labelD = tk.Label(text=f"Difficulty: {difficulty}", fg="yellow")
elif difficulty == "easy":
    labelD = tk.Label(text=f"Difficulty: {difficulty}", fg="green")

labelC.pack()
labelD.pack()
labelQ.pack()
labelA.pack()
new_question.pack()
