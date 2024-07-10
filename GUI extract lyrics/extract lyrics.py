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
