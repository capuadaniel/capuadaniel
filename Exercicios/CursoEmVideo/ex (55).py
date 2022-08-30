sujeito = ['A', 'B', 'C', 'D', 'E']
posicao = 0
maior = 0
menor = 0
for c in range(0,5):
    if c == 1:
        maior = peso
        menor = peso
    else:
    peso = float(input('digite o peso(kg) do sujeito{}: '.format(sujeito[posicao])))
    posicao = posicao + 1

    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print('o maior peso é {} e o menor {}.'.format(maior, menor))


