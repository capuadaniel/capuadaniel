dist = float(input('Qual a distancia da sua viagem em Km? '))
if dist<=200:
    preco = dist*.5
else:
    preco = dist*.45
print('Sua viagem vai custar R${:.2f}'.format(preco))
