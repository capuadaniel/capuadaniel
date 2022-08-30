#ler o nome e peso de varios, guarde em lista e mostre a n cadastrados, lista mais pesados e lista mais leves
# cad de testes ->>> cadastro = [['dan', '89'],['mar', '89'],['eber', '53'],['sil', '53'],['ana', '55']]
cadastro = []
ind = []
pesados = []
leves = []
peso_min = peso_max = 0

print('digite nome e peso para o cadastro (nome vazio encerra)')
while True:
    nome = input('nome: ')
    if nome == '':
        break
    peso = input('peso(kg): ')
    ind.append(nome)
    ind.append(peso)
    cadastro.append(ind[:])
    ind.clear()

pesos = []
for p in cadastro:
    pesos.append(p[1])
for p in cadastro:
    if p[1] == max(pesos):
        pesados.append(p[0])
    elif p[1] == min(pesos):
        leves.append(p[0])

print(f'o cadastro contém {len(cadastro)} pessoas.')
print(f'o maior peso é {max(pesos)} e quem tem esse peso: {pesados}')
print(f'o menor peso é {min(pesos)} e quem tem esse peso: {leves}')
