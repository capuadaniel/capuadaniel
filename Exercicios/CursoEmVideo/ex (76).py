# tuppla com nome dos produtos e preços depois organize em tabela
itens = ('alabarda', 20, 'cimitarra', 25, 'espada curta', 10,
         'espada grande', 50, 'espada longa', 15, 'machado grande', 30)

print(f'{" Medieval dona Pipua ":=^50}')
for elementos in range(0, len(itens), 2):
    print(f'{itens[elementos].capitalize():-<41} R$', end=' ')
    print(f'{itens[elementos+1]:>.2f} ')