#aumente os anteriores adicionando um parametro oopcional que diz para a função moeda() se ela deve ou não receber o formato
from ex_107 import moeda


p = float(input('Digite o preço R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'o aumento de 10% de {moeda.moeda(p)} é {moeda.aumentar(p, 10, True)}')
print(f'A diminuição de 13% de {moeda.moeda(p)} é {moeda.diminuir(p, 13, True)}')