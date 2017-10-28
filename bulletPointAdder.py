#! python 3
#bulletPointAdder.py - na początku każdego wiersza znajdującego się w schowku dodaje gwiazdki tworzące wypunktowaną listę w art. w Wiki

import pyperclip

text = pyperclip.paste()

#rozdzielić wiersze, dodać gwiazdki
lines = text.split('\n') 
for i in range(len(lines)): #iteracja przez wszystkie indeksy listy "lines"
    lines[i] = '* ' + lines[i]  #dodanie '*'
text = '\n'.join(lines)
pyperclip.copy(text)
