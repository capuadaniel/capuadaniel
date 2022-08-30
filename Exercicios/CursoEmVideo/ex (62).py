print('-'*15)
print('{:^15}'.format('Programa calculador de PA'))
print('-'*15)

quermais = 's'
pa = 0
termos = 10
novotermos = 10
while quermais == 's':
    quermais = 's'
    termos = novotermos
    i = int(input('Informe o primeiro termo: '))
    r = int(input('Informe a razão: '))

    while termos > 0:
        print(i, end=' ')
        i = i+r
        termos -= 1

    quermais = str(input('quer mais?[S/N]')).lower().strip()
    if quermais == 'n':
        print('fim')
    else:
        novotermos = int(input('quantos termos vc quer ver dessa nova PA? '))
