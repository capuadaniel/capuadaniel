a = float(input('lado 1: '))
b = float(input('lado 2: '))
c = float(input('lado 3: '))

#quem é o maior?
maior = a
outro1 = b
outro2 = c
if b > a and b > c:
    maior = b
    outro1 = a
    outro2 = c
elif c > a and c > b:
    maior = c
    outro1 = a
    outro2 = b

#faz triangulo?
if (outro1+outro2) <= maior:
    print('Nem é triangulo')
elif a == b and b == c:
    print('Triangulo Equilátero')
elif a == b or b == c or a == c:
    print('Triângulo Isóceles')
elif a != b and b!= c and a!=c:
    print('Trinângulo Escaleno')
else:
    print('É triangulo.')

#alternativo ===================================================

'''
a = float(input('lado 1: '))
b = float(input('lado 2: '))
c = float(input('lado 3: '))

if a >= b + c or b >= a + c or c >= b + a :
    print('Nem é triangulo')
elif a == b and b == c:
    print('Triangulo Equilátero')
elif a == b or b == c or a == c:
    print('Triângulo Isóceles')
elif a != b and b!= c and a!=c:
    print('Trinângulo Escaleno')
else:
    print('É triangulo.')

'''
