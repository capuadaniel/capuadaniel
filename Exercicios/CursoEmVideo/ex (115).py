from ex115_modulo import *
from UtilidadesCeV.dados import leiaInt

#preSets
pessoanova = []
if existearquivo('arquivo.txt') == False:
    criaarquivo('arquivo.txt')
registro = 'arquivo.txt'
entrada = ''


while True:
    #sai do programa caso ja tenha visto a lista
    if entrada == 3:
        print(f'\n \033[44m FINALIZADO \033[m')
        break

    #MOSTRA MENU e TRATA ERROS DE ENTRADA
    cabecalho('Menu principal')
    menu('Ver cadastro', 'Adicionar pessoa', 'Sair')

    while True:
        try:
            entrada = int(input('Sua opção:'))
            if entrada < 1 or entrada > 3:
                print(f'\033[31m ERRO, Opção inválida! \033[m')
                continue
            else:
                break
        except (ValueError, TypeError, KeyError):
            print(f'\033[31m ERRO, Opção inválida! \033[m')
            continue
#OPÇÔES
    if entrada == 1:
        lerCadastro('arquivo.txt')
        while True:
            continuar = input('Voltar ao menu? S/N').upper()
            if continuar in "S":
                break
            else:
                entrada = 3
                break
    elif entrada == 2:
            cabecalho("Adicionar cadastro")
            # lendo dados
            nome = input("Nome: ").title().strip().replace('  ',' ')
            idade = leiaInt("Idade: ")

            #gravando dados no arquivo.txt através da lista pessoanova
            cadastrar(registro, nome, idade)

    elif entrada == 3:
        print(f'\n \033[44m FINALIZADO \033[m')
        break
    else:
        print("entrada")