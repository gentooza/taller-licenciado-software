#!/bin/python3
'''
    Copyright 2022 Joaquín Cuéllar.
    
    This file is part of Hola Mundo Especial.

    Hola Mundo Especial is free software: you can redistribute it and/or modify it 
    under the terms of the GNU General Public License as published by the Free Software Foundation, 
    either version 3 of the License, or (at your option) any later version.

    Hola Mundo Especial is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
    without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
    See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along with Hola Mundo Especial. 
    If not, see <https://www.gnu.org/licenses/>.
'''

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
