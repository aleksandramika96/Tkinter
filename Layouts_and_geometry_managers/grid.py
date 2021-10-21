# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 16:46:09 2021

@author: a.mika2
"""


#libraries
import tkinter as tk

window = tk.Tk()

#grid
for x in range(3):
    for y in range(3):
        label = tk.Label(window, text=f'Row {x}\nColumn {y}')
        label.grid(row=x, column=y)

label = tk.Label(window, text=f'This is a wide label - 3 columns\n', relief=tk.RAISED, borderwidth=1)
label.grid(row=3, column=0, columnspan=3)
        
window.mainloop()