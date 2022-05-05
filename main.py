from tkinter import *
from tkinter import ttk
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




def translationOperation():
    resultText.delete(1.0, END)
    
    # Accessing text to be translated
    textToBeTranslated = entryText.get(1.0, END)
    text = TextBlob(textToBeTranslated)
    
    # Finding corresponding key from value in comboboxes
    for key, value in languages.items():
        if (value == entryCombo.get()):
            from_key = key
        if (value == resultCombo.get()):
            to_key = key
    
    textTranslated = text.translate(from_lang=from_key, to=to_key)
    resultText.insert(END, textTranslated)


# Text Box i.e 'Text-to-Translate' input field
entryText = Text(root, height=10, width=45)
entryText.grid(row=0, column=0, padx=10, pady=20)

# Translate Button
translateButton = Button(root, text="Translate", font=(
    "Helvetica", 16), command=translationOperation)
translateButton.grid(row=0, column=1, padx=20, pady=10)

# Text Box i.e 'Translated text'
resultText = Text(root, height=10, width=45)
resultText.grid(row=0, column=2, padx=10, pady=20)




# Making combo box -> need to import ttk

# Initial to be translated language mode
entryCombo = ttk.Combobox(root, value=listOfLanguages)
entryCombo.current(21)
entryCombo.bind("<<ComboboxSelected>>")
entryCombo.place(x=60, y=200)

# Final Translated language mode
resultCombo = ttk.Combobox(root, value=listOfLanguages)
resultCombo.current(21)
resultCombo.bind("<<ComboboxSelected>>")
resultCombo.place(x=700, y=200)


root.mainloop()
