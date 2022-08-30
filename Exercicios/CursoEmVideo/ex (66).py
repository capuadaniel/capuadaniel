#leia varios n int e pare no 999 mostre a soma
n = s = c = 0
while True:
    n = int(input('digite um numero: '))
    if n == 999:
        break
    s = s + n
    c = c+1
print(f'Você digitou {c} numeros e a soma deles foi {s}.')

