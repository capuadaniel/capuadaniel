print('-'*15)
print('{:^15}'.format('Programa calculador de PA'))
print('-'*15)
i = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))

for PA in range(i, i+(10*r), r):
    print(PA, ' ', end='')
