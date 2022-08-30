#Adapte o cógigo anterior para uma função moeda() que use os valores com um valor monetário formatado.
#Crie um modulo chamado moeda.moeda.py que tenha funções aumentar() diminuir() dobro() metade() e faça um programa que use algumas dessas funções.
from ex_107 import moeda


p = float(input('Digite o preço R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'o aumento de 10% de {moeda.moeda(p)} é {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'A diminuição de 13% de {moeda.moeda(p)} é {moeda.moeda(moeda.diminuir(p, 13))}')