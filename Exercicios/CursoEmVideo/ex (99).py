#Faça a função maior() que recebe varios parametros int, ela deve retornar o maior.
from random import randint as rd

def maior(n):
    m = max(n)
    print(m)

list = (rd(0,10),rd(0,10),rd(0,10),rd(0,10),rd(0,10),rd(0,10),rd(0,10),rd(0,10))

print(f'o maior valor da lista {list} é:')
maior(list)