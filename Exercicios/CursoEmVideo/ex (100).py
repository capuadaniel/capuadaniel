#faça uma lista Numeros e as funções Sorteia() e Somapar() que sorteiam 5 numeros (0,10) e os colocam na lista, e somam os pares da lista e mostra o valor.
from random import randint as rd

def sorteia(lista):
    print (f'sorteando valores para a lista: ', end='')
    for j in range(0,5):
        n = rd(1,10)
        lista.append(n)
        print(n, end=' ')
    print (f' PRONTO!')

def somapar(lista):
    s = 0
    for n in lista:
        if n % 2 == 0:
            s += n
    print(f'A soma dos valores pares de {lista} é {s}')

lista = []
sorteia(lista)
somapar(lista)