from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry('400x400')

def comboclick(event):
    print(myCombo.get())
    pass
options = [
    'a',
    'b',
    'c',
    'd',
    'e'
]
var = StringVar()
myCombo = ttk.Combobox(root, value = options, cursor="star")
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", comboclick)
myCombo.pack()

myButton = Button(root, text = "Change cursor", cursor = "star")

myButton.pack()


root.mainloop()