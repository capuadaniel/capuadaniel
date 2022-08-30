# crie um programa em que 4 resultados joguem um dado e os resultados sejam guardados num dicionario,
# depois mostre um rank pelas jogadas e acuse o jogador vencedor (quem tirou o maior) indicando seus resultados
from random import randint as ri
from operator import itemgetter
resultados = {'Daniel': ri(1,6),
             'Gustavo': ri(1,6),
             'Renata': ri(1,6),
             'Silvia': ri(1,6)}

print('\n', '         RESULTADOS           ')
for k,v in resultados.items():
    print(f'{k} tirou o dado {v}')

print('\n', '          RANKING           ')

contador = 1
resultados = sorted(resultados.items(), key=itemgetter(1), reverse=True)
for k,v in resultados:
    print(f'    O {contador}º lugar vai para {k}')
    contador += 1

#alternativamente usando enumerate ja que resultados passa a ser uma lista:

'''
for i,v in enumerate(resultados):
    print(f'    O {i+1}º lugar vai para {v[0]}')
'''