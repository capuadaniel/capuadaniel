import random

num = ['1','2','3','4','5']
num = random.choice(num)

print('vamos jogar o jogo da advinhação eu estou pensando um numero entre 1 e 5')
resposta = str(input('você sabe qual é? : '))

if resposta == num:
    print('Acertou!')
else:
    print('Errou!')

print('Eu estava pensando no numero {}!' .format(num))
