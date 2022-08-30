#gerar 5 numeros aleatórios e colocar na tupla, listar maior e menor
from random import randint as rd
n = (rd(0, 10), rd(0, 10), rd(0, 10), rd(0, 10), rd(0, 10))

# lista com parenteses
print(f'\nOs n sorteados foram {n}.')

# lista sem parenteses
print('\nOs n sorteados foram: ', end='')
for c in n:
    print(f'{c} ', end='')

print('')
maior = max(n)
menor = min(n)

print(f'\nO maior foi {maior} e o menor foi {menor}.')