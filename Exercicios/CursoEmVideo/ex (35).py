a = float(input('digite o comprimento da reta 1: '))
b = float(input('digite o comprimento da reta 2: '))
c = float(input('digite o comprimento da reta 3: '))

maior = a
outro1 = b
outro2 = c
if b > a and b > c:
    maior = b
    outro1 = a
    outro2 = c
if c > a and c > b:
    maior = c
    outro1 = a
    outro2 = b

if outro1 + outro2 > maior:
    print('Essas retas podem formar triangulo')
else:
    print('Essas retas não podem formar triangulo')
