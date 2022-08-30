#leia varios mostre a media o maior e o menor e se quer mais
soma = 0
entradas = 0
n = (input('digite um numero para o pool (ou digite R para ver os resultados): '))
menor = n
maior = n
fim = False
continuar = 's'

while n != 'r':
    soma = soma + int(n)
    entradas = entradas + 1

    if n > maior:
        maior = n
    if n < menor:
        menor = n

    n = (input('digite um numero para o pool (ou digite R para ver os resultados): '))

print('O maior nº foi {} e o menor {}. A média dos nº é {}.'.format(maior, menor, soma/entradas))
