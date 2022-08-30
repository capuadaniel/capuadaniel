n1 = float(input('Numero 1: '))
n2 = float(input('Numero 2: '))

if n1 > n2:
    print('{} é maior que {}.'.format(n1, n2))
elif n2 > n1:
    print('{} é maior que {}.'.format(n2, n1))
else:
    print('Não há um numero maior entre estes dois')
