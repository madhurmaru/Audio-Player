import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pygame

class MusicPlayerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")
        
        self.playlist = []
        self.current_song_index = 0
        
        self.paused = False
        
        pygame.init()
        
        self.create_widgets()
        
    def create_widgets(self):
        self.song_label = tk.Label(self.master, text="No song playing", font=("Arial", 14))
        self.song_label.pack(pady=10)
        
        self.load_button = tk.Button(self.master, text="Load Song", command=self.load_song, font=("Arial", 12))
        self.load_button.pack(pady=5)
        
        self.play_button = tk.Button(self.master, text="Play", command=self.play_pause_song, font=("Arial", 12))
        self.play_button.pack(pady=5)
        
        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_song, font=("Arial", 12))
        self.stop_button.pack(pady=5)
        
        self.timeline = ttk.Scale(self.master, from_=0, to=100, orient=tk.HORIZONTAL, command=self.update_timeline, length=300)
        self.timeline.pack(pady=10)
        
        self.volume_label = tk.Label(self.master, text="Volume:", font=("Arial", 12))
        self.volume_label.pack()
        
        self.volume_scale = ttk.Scale(self.master, from_=0, to=1, orient=tk.HORIZONTAL, command=self.update_volume, length=150)
        self.volume_scale.set(0.5)
        self.volume_scale.pack(pady=5)
        
        pygame.mixer.music.set_volume(0.5)
        
    def load_song(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if file_path:
            pygame.mixer.music.load(file_path)
            self.playlist.append(file_path)
            self.current_song_index = len(self.playlist) - 1
            self.song_label.config(text="Now Playing: " + file_path.split("/")[-1]) # Display only the file name
            self.timeline.config(to=pygame.mixer.Sound(file_path).get_length())
            
    def play_pause_song(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()
            self.paused = False
        elif self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            pygame.mixer.music.pause()
            self.paused = True
            
    def stop_song(self):
        pygame.mixer.music.stop()
        self.paused = False
        
    def update_timeline(self, value):
        pygame.mixer.music.set_pos(float(value))
        
    def update_volume(self, value):
        pygame.mixer.music.set_volume(float(value))

def main():
    root = tk.Tk()
    root.geometry("400x300")
    app = MusicPlayerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
