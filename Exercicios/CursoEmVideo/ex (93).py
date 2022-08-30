#crie um programa que gerencie um jogador de futebol e registre, o nome, numero de partidas e numero de gols para cada
#partida jogada e depois printe o aproveitamento descrevendo os dados.
jogador={}
gols = []
jogador['nome'] = str(input('Nome: '))
jogador['n_partidas'] = int(input('Quantas partidas já jogou:'))
for j in range(0, jogador['n_partidas']):
    gols.append(int(input(f'Quantos gols fez na {j + 1}ª partida?')))
jogador['gols'] = gols[:]

somagol = 0
for v in jogador['gols']:
    somagol = somagol + int(v)
jogador['total de gols'] = somagol
#alteranativamente
#jogador['total de gols'] = sum(gols)

#exibindo resultados
print('-='*80)
print(jogador)
print('-='*80)
for k, v in jogador.items():
    print(f'O campo {k} tem valor: {v}.')
print('-=' * 80)
print(f'O jogador {jogador["nome"]} jogou: {len(jogador["gols"])} partidas')
for k, v in enumerate(jogador['gols']):
    print(f'   ==> Na partida {k+1} fez {v} gols.')
print(f'Foi um total de {jogador["total de gols"]} gols')