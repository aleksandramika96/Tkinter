# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 10:45:42 2021

@author: a.mika2
"""

import tkinter as tk
window=tk.Tk()

window.geometry("510x600")
window.resizable(False,False)

global label
label = tk.Label(window, text="Please ensure that you use the correct data type", fg='red')

def submit():
    try:
        print(f'Entry:  {str_entry_var.get()}')
        print(f'Password Entry: {int_entry_var.get()}')
        print(f'Radio Buttons:  {double_entry_var.get()}')
        print(f'Check Button 1:  {double_entry_var.get()}')
        print(f'Check Button 2:  {boolean_entry_var.get()}')
    except:
        label.pack()
    else:
        label.pack_forget()

str_entry_var=tk.StringVar()
str_entry=tk.Entry(window,textvariable=str_entry_var)
str_entry.pack()

int_entry_var=tk.IntVar()
int_entry=tk.Entry(window,textvariable=int_entry_var)
int_entry.pack()

double_entry_var=tk.DoubleVar()
double_entry=tk.Entry(window,textvariable=double_entry_var)
double_entry.pack()

boolean_entry_var=tk.BooleanVar()
boolean_entry=tk.Entry(window,textvariable=boolean_entry_var)
boolean_entry.pack()

button=tk.Button(window, text='Submit', command=submit)
button.pack()

window.mainloop()