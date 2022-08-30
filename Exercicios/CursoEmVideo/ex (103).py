#Ficha() recebe nome e gols, o programa deve informar os dads do jogador, mesmo que falte alguma informação.
def ficha(nome='desconhecido', gols='0'):
    g = str(gols)
    if g.isnumeric() == False:
        g = '0'
    print(f'O nome do jogador é {nome.capitalize()} e seus gols registrados são {g}.')

#lista de opções suportadas
ficha('daniel', 10)
ficha(gols=10)
ficha('daniel')
ficha()
ficha('daniel', 't')