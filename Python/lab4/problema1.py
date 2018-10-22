""""Sa se scrie o functie ce va ordona o lista de tuple
 de stringuri in functie de al 3-lea caracter al celui de-al doilea element din tupla."""

def f(my_list):
    return sorted(my_list,key=lambda x:x[1][2])
    #sorted(iterabil) - nu modifica iterabilul ci returneaza alt obiect sortat
    #iterabil.sort - modifica in-place, adica modifica obietul meu

lista_mea=[('abc','bcd'),('abc','zza')]
print(f())
