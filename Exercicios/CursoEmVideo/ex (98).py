#faça função contador que receba 3 parametros e conte 3 contagens a- 1 a 10 de um em 1, b de 10 a 0 de 2 em 2 e uma personalizada onde o
# usuario dis o incio o fim e o passo. Aqui o inicio pode ser maior ou menor eo passo pode ser inclusive negativo ou zero
from time import sleep

def contador(a,b,c):
    for n in range (0,10):
        print(n+1, end=' - ')
        sleep(0.1)
    print('FIM')
    print ('-'*47)

    for n in range (10,0,-1):
        print(n, end=' - ')
        sleep(0.1)
    print('FIM')
    print ('-'*47)


#personalizado
    if c == 0:
        c = 1
    if c > 0 and a > b:
            i = a-1
            f = b-2
            p = -c
    elif c > 0 and b > a:
            i = a-1
            f = b
            p = c
    if c < 0 and a > b:
            i = b-1
            f = a
            p = -c
    elif c < 0 and b > a:
            i = b-1
            f = a-2
            p = c

    for n in range (i,f,p):
        print(n+1, end=' - ')
        sleep(0.1)
    print('FIM')
    print ('-'*47)

print('Sua vez de definir os valores')
i = int(input('Defina o inicio da contagem: '))
f = int(input('Defina o fim da contagem: '))
p = int(input('Defina o passo da contagem: '))
contador(i,f,p)