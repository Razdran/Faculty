
def fbn(n):
    """returneaza al n-lea numar fibonnaci 0 1 1 2 3 """
    if n==1 :
        return 0
    if n==2 :
        return 1
    n1=0
    n2=1
    for i in range(n-1):
        n3=n1+n2
        n1=n2
        n2=n3
    return n3

def is_prime(n):
    for i in range(2,n//2):
        if n%i == 0 :
            return False
    return True

"""convert a text from camelCase into lowercase_with_underscores"""

def upercase_lowercase(string):
    result=""
    if string[0].isupper():
        result=string[0].lower()
    for i in string[1:]:
        if i.isupper():
            result += '_'
            result += i.lower()
    return result

"""scrieti o functie care primeste 3 parametri: un path nivelul de adancime si nr de frunze si creaza un tree de directoare in path
de forma: dir1/dir2/dir3/ frunze1.txt, frunze2.txt ... frunzen.txt"""

import os
def makeLeafs(path,nrfrunze):
    for i in range(nrfrunze):
        name=os.path.join(path,"frunza{}.txt".format(i))
        f=open(name,"w")
        f.close()

def makeDir(path,top,nivel, nrfrunze):
    if nivel>0:
        dir_name="dir" + str(top-nivel)
        dir_path = os.path.join(path,dir_name)
        os.mkdir(dir_path)
        makeDir(dir_path,top,nivel-1,nrfrunze)
    else:
        makeLeafs(path,nr_frunze)

def functie(path,nivel,nrfrunze):
    makeDir(path,nivel,nivel,nr_frunze)
""" scrieti o functie care primeste un path si un nr size si creza in path un fisier cu dimensiunea "size" bytes(un caracter are un byte)"""

def createfile(path,size):
    fd=open(path,"w")
    fd.write("0"*size)
    fd.close()
