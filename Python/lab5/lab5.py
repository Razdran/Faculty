"""1.create a module that contains a function named "sort__uuids".This function reads the file sample.txt 
, and sorts the lines base on the string that is between the first and the second dash(-)."""

def sort__uuids():
    fd = open('sample.txt','r')
    try:
        uuids = fd.readlines()
        uuids.sort(key = Lambda uuid: uuid.split('-')[1])
        return uuids
    except Exception as e:
        pass
        print(e)
"""problema 3 laborator"""
def problema_3():
    fd = open('operatii.txt','r')
    lines= fd.readlines()
    fd.close()
    for line in lines:
        a,b,c = line.strip()
        """..nu e terminata.."""

"""problema 4-parcurgerea recursiva a directoarelor"""
import sys
import os
def parcurge_recursiv(path):
    s= os.listdir(path)
    print(s)
    for f in s:
        if os.path.isdir(os.path.join(path,f)):
            parcurge_recursiv(os.path)
 """exista o functie care face exact ce face problema 4"""
 for root, dirs, files in os.walk(r'path/dir/dir/...')                      
 """problema 5 scrieti un script care primeste un path si afiseaza primii 4096 biti daca pathul duce la un fisier, intratrile din acesta daca
 pathul este un director si un mesaj de eroare daca pathul este invalid"""

import os
 def pb2(path):
     if os.path.isfile(path):
         fd=open(path,'r')
         print(fd.read(4096))
         fd.close()
         """... nu e terminata..."""


"""problema 6 Scrieti un script care primeste 3 parametri de la consola. Primul va fi un path catre un fisier, al doilea va fi un path 
catre un director iar al treilea va fi dimensiunea unui buffer. Scriptul va copia fisierul dat ca paarametru in directorul dat ca parametru"""

def pb6(path_to_file,path_to_dir,size):
    fd = open(path_to_file,'r')
    file=fd.read(size)
    fd2= open(os.path.join(path_to_dir,os.path.basename(path_to_file)),'w')
    
    while file :
        fd2.write(file)
        file=fd.read(size)
    fd2.close()
    fd.close()
   