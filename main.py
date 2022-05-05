from tkinter import *
from tkinter import ttk
import googletrans


root = Tk()
root.title('Translator App')
root.iconbitmap('static/translator_icon.ico')
root.geometry('915x430')


def entryComboClick(event):
    pass

def resultComboClick(event):
    pass
def translationOperation():
    pass

# Text Box i.e 'Text-to-Translate' input field
entryText = Text(root, height = 10, width = 45)
entryText.grid(row = 0, column = 0, padx = 10, pady = 20)

# Translate Button
translateButton = Button (root, text = "Translate", font=("Helvetica", 16), command = translationOperation)
translateButton.grid(row = 0, column = 1, padx = 20, pady = 10)

# Text Box i.e 'Translated text'
resultText = Text(root, height =10, width = 45)
resultText.grid(row = 0, column = 2 , padx = 10, pady = 20)


# Appending countries name in list through googletrans api

languages = googletrans.LANGUAGES
listOfLanguages = []
for key, value in languages.items():
    listOfLanguages.append(value)


# Making combo box -> need to import ttk 

# Initial to be translated language mode
entryCombo = ttk.Combobox(root, value = listOfLanguages)
entryCombo.current(21)
entryCombo.bind("<<ComboboxSelected>>", entryComboClick)
entryCombo.place(x = 60, y = 200)

# Final Translated language mode
resultCombo = ttk.Combobox(root, value = listOfLanguages)
resultCombo.current(21)
resultCombo.bind("<<ComboboxSelected>>", resultComboClick)
resultCombo.place(x = 700, y = 200)


root.mainloop()