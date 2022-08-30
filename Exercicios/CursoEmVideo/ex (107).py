#Crie um modulo chamado moeda.py que tenha funções aumentar() diminuir() dobro() metade() e faça um programa que use algumas dessas funções.
from ex_107 import moeda


p = float(input('Digite o preço R$'))
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'o aumento de 10% de R${p} é R${moeda.aumentar(p, 10)}')
print(f'A diminuição de 13% de R${p} é R${moeda.diminuir(p, 13)}')
