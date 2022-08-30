media = 0
idade20 = 0
hmaisvelho = ''
maioridade = 0
for c in range(1,5):
    nome = str(input('nome do sujeito{}:'.format(c))).strip()
    idade = int(input('qual sua idade?'))
    genero = int(input('qual seu genero? [1]Feminino [2]Masculino [3]Outros' ))

    if idade > maioridade and genero == 2:
        maioridade = idade
        hmaisvelho = nome
    media += idade
    if idade < 20 and genero == 1:
        idade20 +=1

media = float(media/(c+1))
print('O nome do homem mais velho é {}, a média de idade é {} e {} mulheres tem menos de 20 anos.'.format(hmaisvelho, media, idade20))
