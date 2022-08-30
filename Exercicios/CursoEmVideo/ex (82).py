#leia varios e crie 2 listas extras com apenas impares e apenas pares, mostre elas
completa = []
pares = []
impares = []
while True:
    n = input('Digite um valor: ')
    if n.isnumeric() == True:
        if int(n) % 2 == 0:
            completa.append(n)
            pares.append(n)
        if int(n) % 2 != 0:
            completa.append(n)
            impares.append(n)
    if n.isnumeric() == False:
        break
print('='*60)
print('Lista completa: ', completa)
print('Pares: ', pares)
print('Impares: ', impares)