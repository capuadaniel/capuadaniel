#Faça um minisistema que use o interactive help para mostrar a ajuda sobre um comando,
# se o user digtar "fechar" o programa fecha. OBS use cores.
print('iniciando a AJUDONA')

while True:
    entrada = input('\033[7;94m Sobre o que você quer ajuda? ("fechar" para sair) \033[m ')
    if entrada == 'fechar':
        print(' \033[7;31m FINALIZADO \033[m')
        break
    print(f'\033[7;12m')
    help(entrada)

