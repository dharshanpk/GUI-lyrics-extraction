# GUI-lyrics-extraction
1. Introduction
Purpose
The purpose of this project is to design a graphical user interface (GUI) application that can extract lyrics from songs using Python. The application will use an API to fetch lyrics and display them on the interface.

Prerequisites
Basic knowledge of Python
tkinter library for GUI
requests library for making HTTP requests
2. Project Structure
Files
lyrics_gui.py: Contains the main code for the GUI application.
3. Detailed Steps
Step 1: Install Required Libraries
Make sure you have the necessary libraries installed.

bash
pip install requests
Step 2: Import Required Libraries
Import the necessary libraries including Tkinter and Requests.


import tkinter as tk
from tkinter import messagebox
import requests
Step 3: Set Up the GUI
Create the main window and set up the GUI layout.


# Create the main window
root = tk.Tk()
root.title("Lyrics Extractor")

# Set up the GUI layout
label = tk.Label(root, text="Enter Song Name and Artist:")
label.pack(pady=10)

entry_song = tk.Entry(root, width=50)
entry_song.pack(pady=5)
entry_song.insert(0, "Song Name")

entry_artist = tk.Entry(root, width=50)
entry_artist.pack(pady=5)
entry_artist.insert(0, "Artist Name")

text_area = tk.Text(root, wrap='word', height=15, width=60)
text_area.pack(pady=10)
Step 4: Create the Function to Fetch Lyrics
Define a function to fetch lyrics from an API.


def fetch_lyrics(song, artist):
    api_url = f"https://api.lyrics.ovh/v1/{artist}/{song}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("lyrics", "Lyrics not found.")
    else:
        return "Lyrics not found."
Step 5: Create the Button and Function to Display Lyrics
Add a button to the GUI and define the function to display lyrics.


def display_lyrics():
    song = entry_song.get()
    artist = entry_artist.get()
    lyrics = fetch_lyrics(song, artist)
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, lyrics)

button = tk.Button(root, text="Get Lyrics", command=display_lyrics)
button.pack(pady=10)
Step 6: Run the Application
Run the Tkinter main loop to start the application.


root.mainloop()

Complete Code
Here is the complete code for the GUI application:


import tkinter as tk
from tkinter import messagebox
import requests

# Create the main window
root = tk.Tk()
root.title("Lyrics Extractor")

# Set up the GUI layout
label = tk.Label(root, text="Enter Song Name and Artist:")
label.pack(pady=10)

entry_song = tk.Entry(root, width=50)
entry_song.pack(pady=5)
entry_song.insert(0, "Song Name")

entry_artist = tk.Entry(root, width=50)
entry_artist.pack(pady=5)
entry_artist.insert(0, "Artist Name")

text_area = tk.Text(root, wrap='word', height=15, width=60)
text_area.pack(pady=10)

def fetch_lyrics(song, artist):
    api_url = f"https://api.lyrics.ovh/v1/{artist}/{song}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("lyrics", "Lyrics not found.")
    else:
        return "Lyrics not found."

def display_lyrics():
    song = entry_song.get()
    artist = entry_artist.get()
    lyrics = fetch_lyrics(song, artist)
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, lyrics)

button = tk.Button(root, text="Get Lyrics", command=display_lyrics)
button.pack(pady=10)

# Run the application
root.mainloop()
4. Conclusion
This project demonstrated how to create a GUI application to extract lyrics from songs using Python. The application uses Tkinter for the GUI and the lyrics.ovh API to fetch lyrics. This approach can be further enhanced by using other APIs or web scraping techniques for more comprehensive functionality.
