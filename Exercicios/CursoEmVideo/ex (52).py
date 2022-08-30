n = int(input('Digite um número para saber se ele é primo:'))
resultado = 1
for d in range(2, n-1):
    if n % d == 0:
        resultado = 0
if resultado == 1:
    print('é PRIMO!')
else:
    print('NÃO é primo!')
'''
alternativo =================================

#ex 52 plus
for n in range(100000000000000000000000000,1000000000000000000000000000 ):
    resultado = 1
    for d in range(2, n-1):
        if n % d == 0:
            resultado = 0
    if resultado == 1:
        print(n, end=' ')
'''