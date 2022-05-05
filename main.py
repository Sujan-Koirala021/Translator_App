# Simple Translator App using TextBlob and GoogleTrans
# Sujan Koirala, Institute of Engineering, Pulchowk


from email import message
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from textblob import TextBlob
import googletrans


root = Tk()
root.title('Translator App')
root.iconbitmap('static/translator_icon.ico')
root.geometry('915x430')


# Appending countries name in list through googletrans api

languages = googletrans.LANGUAGES
listOfLanguages = []
for key, value in languages.items():
    listOfLanguages.append(value)


def clear():
    # Deleting previous records
    entryText.delete(1.0, END)
    resultText.delete(1.0, END)
    # Setting comboboxes to default
    entryCombo.current(21)
    resultCombo.current(88)


def translationOperation():
    resultText.delete(1.0, END)

    # Accessing text to be translated
    textToBeTranslated = entryText.get(1.0, END)
    text = TextBlob(textToBeTranslated)

    try:
        # Finding corresponding key from value in comboboxes
        for key, value in languages.items():
            if (value == entryCombo.get()):
                from_key = key
            if (value == resultCombo.get()):
                to_key = key

        textTranslated = text.translate(from_lang=from_key, to=to_key)
        resultText.insert(END, textTranslated)

    except Exception as e:
        messagebox.showerror("Translator", e)


# Text Box i.e 'Text-to-Translate' input field
entryText = Text(root, height=10, width=45)
entryText.grid(row=0, column=0, padx=10, pady=20)

# Translate Button
translateButton = Button(root, text="Translate", font=(
    "Helvetica", 16), command=translationOperation)
translateButton.grid(row=0, column=1, padx=20, pady=10)


# Clear Button
clearButton = Button(root, text="Clear", font=(
    "Helvetica", 12), command=clear)
clearButton.place(x=430, y=200)

# Text Box i.e 'Translated text'
resultText = Text(root, height=10, width=45)
resultText.grid(row=0, column=2, padx=10, pady=20)


# Making combo box -> need to import ttk

# Initial to be translated language mode
entryCombo = ttk.Combobox(root, value=listOfLanguages)
# Setting English Language as default (refering the dictionary)
entryCombo.current(21)
entryCombo.bind("<<ComboboxSelected>>")
entryCombo.place(x=60, y=200)

# Final Translated language mode
resultCombo = ttk.Combobox(root, value=listOfLanguages)
# Setting Spanish language as default (refering the dictionary)
resultCombo.current(88)
resultCombo.bind("<<ComboboxSelected>>")
resultCombo.place(x=700, y=200)


root.mainloop()
