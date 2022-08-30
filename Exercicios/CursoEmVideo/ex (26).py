frase = str(input('Escreve uma frase aí:\n')).lower().strip()

#converte a frase para minusculo e todos a com acento ficam sem
frase = frase.replace('á','a')
frase = frase.replace('à','a')
frase = frase.replace('â','a')
frase = frase.replace('â','a')
frase = frase.replace('ä','a')

ndea = frase.count('a')
primeiro = frase.find('a')
ultimo = frase.rfind('a')

print('''
Essa Frase aí tem {} vezes a letra A.
A primeira é no {}ºespaço.
A ultima vez é no {}ºespaço.
'''.format(ndea, primeiro+1, ultimo+1))