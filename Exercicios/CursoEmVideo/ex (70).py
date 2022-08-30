#leina nome e preço de produtos, mostre total gasto, quantos custam mais de 1000 e nome do mais barato
print('*'*30)
print('{:^30}'.format('Mercado bataté'))
print('*'*30)
cont = 1
maiorquemil = soma_compra = 0
continua = preco_produto = nome_mais_barato = nome_produto = 'z'
while True:
    while nome_produto == 'z':
        nome_produto = str(input('Nome do produto: '))
    while preco_produto == 'z':
        preco_produto = (input('Preço do Produto:R$ ')).strip()
        if preco_produto.isnumeric() == True:
            preco_produto = float(preco_produto)
        else:
            preco_produto = 'z'
    soma_compra = soma_compra + preco_produto
    if cont == 1:
        menor = preco_produto
        cont -=1
        nome_mais_barato = nome_produto
    if preco_produto < menor:
        menor = preco_produto
        nome_mais_barato = nome_produto
    if preco_produto >= 1000:
        maiorquemil += 1
    while continua not in "sn":
        continua = str(input('Mais um produto? [s/n]')[0]).lower().strip()
    if str(continua) == 'n':
        break
    continua = preco_produto = nome_produto = 'z'
print(f'\nO valor total da compra é R${soma_compra}.')
print(f'Esta compra contém {maiorquemil} compras de mais de mil reais.')
print(f'O item mais barato é o {nome_mais_barato}, por R${menor:.2f}.')