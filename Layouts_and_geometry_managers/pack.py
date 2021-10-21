# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 16:41:38 2021

@author: a.mika2
"""

#libraries
import tkinter as tk

window = tk.Tk()

#pack
w = tk.Label(window, text='Tekst 1')
w.pack(padx=20, pady=20, side=tk.LEFT)
w = tk.Label(window, text='Tekst 2')
w.pack(padx=20, pady=20, side=tk.LEFT)
w = tk.Label(window, text='Tekst 3')
w.pack(padx=20, pady=20, side=tk.LEFT)

window.mainloop()