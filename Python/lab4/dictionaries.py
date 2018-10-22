## Dictionarele sunt seturi de tipul cheie-valoare
## Cheia trebuie sa fie neaparat un obiect de tip hashabel  iar valoarea poate fi orice

d=dict()
d={1:'a',2:'b',3:'c','r':4,(1,2,3):"a tuple as key"}

##pentru iterare

print(d.keys())
print(d.values())

for k in d.keys():
    print(k)

for k in d.items():
    print(k)
