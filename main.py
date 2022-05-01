from tkinter import *

root = Tk()
root.title('Translator App')
root.iconbitmap('static/translator_icon.ico')
root.geometry('915x330')

# Text Boxes

entryText = Text(root, height = 10, width = 45)
entryText.grid(row = 0, column = 0, padx = 10, pady = 20)

translateButton = Button (root, text = "Translate", font=("Helvetica", 16))
translateButton.grid(row = 0, column = 1, padx = 20, pady = 10)

resultText = Text(root, height =10, width = 45)
resultText.grid(row = 0, column = 2 , padx = 10, pady = 20)



root.mainloop()