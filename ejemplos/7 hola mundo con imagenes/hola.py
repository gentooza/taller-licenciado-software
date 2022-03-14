#!/bin/python3

import tkinter as tk
from PIL import ImageTk, Image
import os

root = tk.Tk()

message = tk.Label(root, text="Hola mundo!")
message.pack()

img = ImageTk.PhotoImage(Image.open("images/hola.png"))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

root.mainloop()
