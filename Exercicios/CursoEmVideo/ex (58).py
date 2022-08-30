import random
num = random.randint(1, 10)
pal = 1
print('vamos jogar o jogo da advinhação eu estou pensando um numero entre 1 e 10')
resposta = int(input('tente advinhar qual é : '))


while resposta != num:
    pal += 1
    if resposta > num:
        resposta = int(input('Era menos, tente de novo: '))
    else:
        resposta = int(input('Era mais, tente de novo: '))

print('Eu estava pensando no numero {}! Você precisou de {} palpites para descobrir!' .format(num, pal))

