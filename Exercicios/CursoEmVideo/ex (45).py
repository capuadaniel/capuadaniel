import random
print(' *' * 15,'\n       Jogue JanKenPo!\n',' *' * 15)
vc = int(input('Qual opção você vai jogar?\n(1) pedra\n(2) papel\n(3) tesoura\nResposta: '))
# pc escolhe sua opção
pc = [1, 2, 3]
pc = random.choice(pc)
if vc == pc:
    print('Empate!')
elif vc == 1 and pc == 3:
    print('Você ganhou!')
elif vc == 3 and pc == 1:
    print('Você perdeu!')
elif vc > pc:
    print("Você ganhou!")
elif vc < pc:
    print("Você perdeu!")
