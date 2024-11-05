

import tkinter as tk

class OpeningScreen:
    def __init__(self, master, set_map_func, set_difficulty_func):
        self.master = master
        self.set_map_func = set_map_func
        self.set_difficulty_func = set_difficulty_func

        master.title("Opening Screen")

        self.choose_map_button = tk.Button(master, text="Choose Map", command=self.choose_map)
        self.choose_map_button.pack()

        self.choose_difficulty_button = tk.Button(master, text="Choose Difficulty", command=self.choose_difficulty)
        self.choose_difficulty_button.pack()

    def choose_map(self):
        self.set_map_func()

    def choose_difficulty(self):
        self.set_difficulty_func()

root = tk.Tk()

def set_map():
    # Function to set the game map
    pass

def set_difficulty():
    # Function to set the game difficulty level
    pass

opening_screen = OpeningScreen(root, set_map, set_difficulty)
root.mainloop()
