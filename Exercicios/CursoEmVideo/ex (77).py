#tupla com palavras mostrar vogais de cada uma
palavras = ('roupa', 'sapato', 'cagatto', 'pipua', 'lua', 'sol', 'frio', 'calor', 'calos', 'pés', 'eletricidade', 'tomada', 'conquista', 'flerte', 'paixão', 'sexo', 'toalha')

for elemento in palavras:
    print(f'Na palavra {elemento} temos as vogais:', end=' ')
    for letra in elemento:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print('')