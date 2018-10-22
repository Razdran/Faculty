""""1.sa se implementeze functia prob1(n).Functia primeste un parametru n nr nat mai mare ca 0. Functia va returna o lista
cu primele n numere naturale mai mari strict decat 30. Spre exemplu problema1(3) va returna [31],[32],[33]"""

def problema1(n):
    return[i+31 for i in range(n)]
print(problema1(3))
"""2.sa se implementeze fct problema 2(bigstr,smallstr).Functia primeste ca parametri doua stringuri"""
def problema2(big_string,small_string):
    if big_string.count(small_string)==2:
        return True
    else:
        return False


"""3. sa se impl fct care primeste un nr nat x >1 fct va returna rezultatul polinomului 2*pow(x,3)-pow(x,2)-x+3.Unde 
pow(x,2) repr x la puterea a doua"""
def problema3(x):
    return 2*pow(x,3)-pow(x,2)-x+3

"""4. sa se implementeze"""