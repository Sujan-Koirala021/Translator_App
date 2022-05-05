import googletrans
languages = googletrans.LANGUAGES
listOfLanguages = []
for key, value in languages.items():
    listOfLanguages.append(value)
print(listOfLanguages)