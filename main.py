from tkinter import *
from tkinter import ttk
import tkinter
import numpy as np 

num=""
def entry_delete():
  global num
  entry.delete(0, END)
  num=""
def entry_update(text):
  global num
  num = num + str(text)
  entry.insert(999,text) #display text to the right
def entry_calculate():
  global num
  equals = str(eval(num))
  equals = "{:.6}".format(equals)
  input.set(equals)
  
win=tkinter.Tk()
win.title("Calculator")
win.geometry("725x800")

input=StringVar()

entry= Entry(win, width= 30, textvariable=input, bg= "white")
entry.grid(row=0, column=1, pady=10, ipady=5, columnspan=4)

Button(text="C", command=entry_delete).grid(row=1, column=1, sticky="ew")
Button(text="%", command=lambda: entry_update("%")).grid(row=1, column=2, sticky="ew")
Button(text="**", command=lambda: entry_update("**")).grid(row=1, column=3, sticky="ew")
Button(text="/", command=lambda: entry_update("/")).grid(row=1, column=4, sticky="ew")

Button(text="7", command=lambda: entry_update(7)).grid(row=2, column=1, sticky="ew")
Button(text="8", command=lambda: entry_update(8)).grid(row=2, column=2, sticky="ew")
Button(text="9", command=lambda: entry_update(9)).grid(row=2, column=3, sticky="ew")
Button(text="*", command=lambda: entry_update("*")).grid(row=2, column=4, sticky="ew")

Button(text="4", command=lambda: entry_update(4)).grid(row=3, column=1, sticky="ew")
Button(text="5", command=lambda: entry_update(5)).grid(row=3, column=2, sticky="ew")
Button(text="6", command=lambda: entry_update(6)).grid(row=3, column=3, sticky="ew")
Button(text="-", command=lambda: entry_update("-")).grid(row=3, column=4, sticky="ew")

Button(text="1", command=lambda: entry_update(1)).grid(row=4, column=1, sticky="ew")
Button(text="2", command=lambda: entry_update(2)).grid(row=4, column=2, sticky="ew")
Button(text="3", command=lambda: entry_update(3)).grid(row=4, column=3, sticky="ew")
Button(text="+", command=lambda: entry_update("+")).grid(row=4, column=4, sticky="ew")

Button(text="0", command=lambda: entry_update(0)).grid(row=5, column=1, columnspan=2, sticky="ew")
Button(text=".", command=lambda: entry_update(".")).grid(row=5, column=3, sticky="ew")
Button(text="=", command=entry_calculate).grid(row=5, column=4, sticky="ew")

win.mainloop()

