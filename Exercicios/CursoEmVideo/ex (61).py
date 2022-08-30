print('-'*15)
print('{:^15}'.format('Programa calculador de PA'))
print('-'*15)
i = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))
pa = 0
termos = 10
pa = i
while termos > 0:
    if termos == 10:

        print(pa, end=' ')
        termos -= 1
    else:
        pa = pa + r
        termos -= 1
        print(pa, end=' ')
#alternativamente
'''
print('-'*15)
print('{:^15}'.format('Programa calculador de PA'))
print('-'*15)
i = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))
pa = 0
termos = 10
pa = i
while termos > 0:
        print(pa, end=' ')
        pa = pa + r
        termos -= 1
'''