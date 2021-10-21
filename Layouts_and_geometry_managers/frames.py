# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 16:52:57 2021

@author: a.mika2
"""

#libraries
import tkinter as tk

window = tk.Tk()
frame = tk.Frame(background='black')
frame.pack(side=tk.BOTTOM)

w = tk.Label(frame, text='Text 1')
w.pack(padx=5, pady=5,)

window.mainloop()
