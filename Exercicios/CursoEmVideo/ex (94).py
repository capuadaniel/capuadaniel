#leia o nome, idade, genero de varias pesssoas guardando em dicios e os dicios numa lista
#no fim mostre: total de cadastrados, média de idade, lista das mulheres, lista pessoas acima da média de idade.
pessoas = []
dados = {}

while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['genero'] = str(input('Genero(M/F/I/A): ')).upper()[0]
        if dados['genero'] in 'MFIA':
            break
        print('Erro, digite M, F, I ou A')
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())

    while True:
        continuar = input('Cadastrar mais um? [S/N]').upper()[0]
        if continuar in 'SN':
            break
        print('Erro, digite S ou N')
    if continuar == 'N':
        break

print('=-'*80)
print(pessoas)
print('=-'*80)

#media de idade
media_idade = 0
for n in pessoas:
    for k, v in n.items():
        if k == 'idade':
            media_idade += v
media_idade = media_idade/ len(pessoas)

#lista dem mulheres
mulheres = []
for n in pessoas:
    for k, v in n.items():
        if str(v) in 'Ff':
            mulheres.append(n['nome'])

#lista de acima da idade
acima_media = []
for n in pessoas:
    for k, v in n.items():
        if k == 'idade' and v > media_idade:
            acima_media.append(n['nome'])

print(f'O total de cadastrados é {len(pessoas)}')
print(f'A média de idade é {media_idade:.2f}')
print(f'As mulheres na lista são {mulheres}.')
print(f'As pessoas acima da média de idade são {acima_media}.')