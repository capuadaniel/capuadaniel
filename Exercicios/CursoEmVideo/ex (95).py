#volte no 93 e agora inclua varios jogadores e de os detalhes de aproveitamento de cada um:
#mostre uma tabela com todos e depois deixe o user entrar  em cada um para ver detalhes, 999 sai.
todos = []
jogador = {}
gols = []
contador = 1

while True:
    jogador['numero'] = contador
    jogador['nome'] = input('Nome do Jogador(a): ')
    jogador['n de jogos'] = input('Número de n de jogos em que participou: ')

    n_partidas = jogador['n de jogos']
    for n in range(0,int(n_partidas)):
        gols.append(input(f'Quantos gols foram feitos na {n+1}ª partida?: '))
        jogador['gols'] = gols
        somagol = 0
        for v in jogador['gols']:
            somagol = somagol + int(v)
        jogador['total de gols'] = somagol

    todos.append(jogador.copy())
    somagol = 0
    gols = []
    maisum = input('Mais um jogador(a)? [S/N]').lower()
    if maisum != 's':
        break
    contador += 1

print(f'{"numero":<15}{"nome":<15}{"n de jogos":<15}{"total de gols":<15}')
for n in todos:
    print(f'{n["numero"]:<15}{n["nome"]:<15}{n["n de jogos"]:<15}{n["total de gols"]:<15}')

print()
detalhes = 1
while detalhes != 0:
    detalhes = input('\nSair [0], ver detalhes de um(a) jogador(a) [n]: ')
    if detalhes.isnumeric() == False or int(detalhes) > len(todos):
        print('Esse(a) jogador(a) não existe.')
        detalhes = input('\nSair [0], ver detalhes de um(a) jogador(a) [n]: ')
    detalhes = int(detalhes)
    print('-=' * 120)
    print(f'Detalhes do jogador {todos[detalhes-1]["nome"].upper()}:')
    for i, j in enumerate(todos[detalhes-1]['gols']):
        print(f'   ==> no jogo {i+1} fez {j} gols')
    print('-=' * 120)

print(' ===== FIM ===== ')
