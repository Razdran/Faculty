"""Scrieti o functie care primeste ca parametru un sir de caractere si returneaza un dictionar in care cheile sunt
caracterele din componenta cirului de caractere iar valorile sunt reprezentate de numarul de aparitii ale
caracterului respecti"""

def ex2(myString):
    d=dict()
    for letter in myString:
        if letter in myString:
            if letter not in d:
                d[letter]= myString.count(letter)
    return d

print(ex2('ana are mere'))