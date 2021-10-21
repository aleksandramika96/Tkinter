# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 10:46:13 2021

@author: a.mika2
"""

import tkinter as tk
window=tk.Tk()

window.geometry("510x600")
window.resizable(False,False)

#---------------Menu--------------------#
def donothing():
   x = 0

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Past", command=donothing)
editmenu.add_command(label="Duplicate Line", command=donothing)
editmenu.add_command(label="Toggle Case", command=donothing)
menubar.add_cascade(label="Edit", menu=editmenu)

window.config(menu=menubar)
#---------------/Menu--------------------#

def submit():
    print(f'Entry:  {entry_var.get()}')
    print(f'Password Entry: {password_entry.get()}')
    print(f'Radio Buttons:  {radio_buttons_var.get()}')
    print(f'Check Button 1:  {check_button1_var.get()}')
    print(f'Check Button 2:  {check_button2_var.get()}')




#---------------titles--------------------#
widgets =['label', 'entry', 'password', 'radio buttons', 'check buttons','button']
x=0
for widget in widgets:
    label = tk.Label(window, text=widget)
    label.grid(row=x, column=0)
    x+=1
#--------------/titles--------------------#

#---------------label--------------------#
label = tk.Label(window, text="Label")
label.grid(row=0, column =1)


#---------------entry--------------------#
entry_var=tk.StringVar()
entry=tk.Entry(window,textvariable=entry_var)
entry.grid(row=1, column =1, )


#---------------password--------------------#
password_entry_var=tk.StringVar()
password_entry=tk.Entry(window, show="*", textvariable=password_entry_var)
password_entry.grid(row=2, column =1)

#---------------radio buttons--------------------#
radio_buttons_var=tk.StringVar()
radio_button_frame=tk.Frame(window)
radio_button_frame.grid(row=3, column =1)
radiobutton1 = tk.Radiobutton(radio_button_frame,
                                   text="Radiobutton 1", value=1, variable=radio_buttons_var)
radiobutton2 = tk.Radiobutton(radio_button_frame,
                                   text="Radiobutton 2", value=2, variable=radio_buttons_var)
radiobutton1.pack()
radiobutton2.pack()


#---------------Check Buttons--------------------#
check_button_frame=tk.Frame(window)
check_button_frame.grid(row=4, column =1)
check_button1_var=tk.StringVar()
checkbutton1 = tk.Checkbutton(check_button_frame,
                                   text="Checkbutton 1", variable=check_button1_var)
checkbutton1.pack()

check_button2_var=tk.StringVar()
checkbutton2 = tk.Checkbutton(check_button_frame,
                                   text="Checkbutton 2", variable=check_button2_var)
checkbutton2.pack()

#---------------Buttons--------------------#
button=tk.Button(window, text='Submit',command=submit)
button.grid(row=5, column=1)


window.mainloop()