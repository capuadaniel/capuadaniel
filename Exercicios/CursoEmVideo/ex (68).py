from random import randint
#jogue par ou impar só interrompe se jog perder e mostra o numero de vitorias
print('='*20,'\n JOGO do Par ou Impar\n','='*20 )
n = pc = soma = c =0
while True:
    n = int(input('digite seu número:'))
    palpite = ' '
    while palpite not in 'pi'
        palpite = str(input('Qual seu palpite [P/I]?')).lower().strip()[0]
    pc = randint(1,5)
    soma = pc + n
    c += 1
    if (soma % 2) == 0 and palpite == 'p': #se PAR CERTO
        print(f'eu escolhi {pc}, e a soma deu {soma}, você venceu.\n Vamos de novo?')

    elif (soma % 2) != 0 and palpite == 'i':  # se IMPAR CERTO
        print(f'eu escolhi {pc}, e a soma deu {soma}, você venceu.\n Vamos de novo?')

    else:  # se ERRAR
        print(f'eu escolhi {pc}, e a soma deu {soma}, você perdeu.\n Até que enfim')
        break
print(f'Jogamos {c} vezes e você venceu {c-1}!')
