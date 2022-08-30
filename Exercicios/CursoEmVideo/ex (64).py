#leia varios int e pare só no 999 no fim mostre quantos e e a soma desconsiderando o 999
n = 0
soma = 0
numeros = 0
while n != 999:
    n = int(input('Digite um numero (999 para parar): '))
    soma = soma + n
    numeros += 1
print('Você digitou {} numeros e a soma deles foi {}.'.format(numeros-1, soma-999))