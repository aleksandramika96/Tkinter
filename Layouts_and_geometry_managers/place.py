# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 16:42:57 2021

@author: a.mika2
"""

#libraries
import tkinter as tk

window = tk.Tk()

#place
w = tk.Label(window, text='Tekst 1',)
w.place(x=0, y=0)
w = tk.Label(window, text='Tekst 2',)
w.place(x=50, y=0)
w = tk.Label(window, text='Tekst 3',)
w.place(x=100, y=0)

window.mainloop()