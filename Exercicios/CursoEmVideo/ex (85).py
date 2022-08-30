#receba 7 valores em uma unica lista sem outras e mostre, lista completa(essa não precisava), pares em ordem e impares em ordem
l_num = []
for c in range(0,7):
    n = input('insira um valor [999 para parar]:')
    if n == '999':
        break
    l_num.append(n)
print('='*60,'\n')
print(f'A lista completa é: {sorted(l_num)}')

print(f'Os pares são: ', end='')
for n in sorted(l_num):
    if int(n) % 2 == 0:
        print(f'{n} ', end='')

print(f'\nOs impares são: ', end='')
for n in sorted(l_num):
    if int(n) % 2 != 0:
        print(f'{n} ', end='')

#<<<<<<<<<<<< alternativamente >>>>>>>>>>>>>>>>>>>
lista = [[],[]]
for c in range(0,7):
    n = int(input('numero para a lista de 7 numeros: '))
    if n % 2 ==0:
        lista[0].append(n)
    if n % 2 != 0:
        lista[1].append(n)
print(f'Os pares são {sorted(lista[0])} e os impares são {sorted(lista[1])}')