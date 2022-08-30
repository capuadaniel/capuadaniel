#leia 4 valores guarde na tupla, diga quantos 9, que posição está o  3 e quais os pares
n1 = float(input('Digite um numero:'))
n2 = float(input('Digite um numero:'))
n3 = float(input('Digite um numero:'))
n4 = float(input('Digite um numero:'))
tupla = (n1, n2, n3, n4)
#quantos 9s
print (f'Dos valores digitados {tupla.count(9)} são "9".')

#posição do 3
if 3 in tupla:
    print (f'Dos valores digitados o "3" está na posição {tupla.index(3)+1}.')
else:
    print ('Não há valores 3 entre os digitados')

#pares ou não
pares = False
print ('Dos valores digitados os pares são: ', end='')
for c in tupla:
    if c % 2 == 0:
        print(f'{c} ', end=' ')
        pares = True
if pares == False:
    print('Nenhum.')
