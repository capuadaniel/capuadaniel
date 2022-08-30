#programa mega sena, quantos jogos serão feitos e sortear 6 numeros entre 1 e 60 cadastrando tudo numa lista composta.
from random import randint
while True:
    n_jogos = input('Quantos jogos vc quer fazer?')
    if n_jogos.isnumeric() == True:
        break
contador = 0
jogos = []
numeros = []

for j in range(0,int(n_jogos)+1):
    for p in range(0,int(n_jogos)+1):
        sorteado = randint(1,60)
        if sorteado not in numeros:
            numeros.append(sorteado)
            contador += 1
        if contador >= 6:
            jogos.append(numeros[:])
            numeros.clear()
            contador = 0
for n in range(0,int(n_jogos)):
    print(f'Seu {n+1}º jogo: {sorted(jogos[n])}')
