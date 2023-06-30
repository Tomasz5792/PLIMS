import tkinter as tk
from tkinter import ttk
#import tkkbootstrap as ttk

#functions
def command_1():
    print("button 1 clicked")

#window
window = tk.Tk()
window.title("PLIMS")
window.geometry("1400x800")


button_1 = tk.Button(window, text = "Click me", command = command_1,width=20,height=2,bg="red",fg="white")
button_1.grid(row=0,column=0,padx=0,pady=0)
#button_1.pack(side=tk.LEFT)

button_2 = tk.Button(window, text = "Click me", command = command_1,width=20,height=2)
button_2.grid(row=0,column=2,padx=0,pady=0)
#button_2.pack(side=tk.LEFT)


window.columnconfigure(0, weight=0)
window.columnconfigure(1, weight=0)
window.columnconfigure(2, weight=0)

#run
window.mainloop()