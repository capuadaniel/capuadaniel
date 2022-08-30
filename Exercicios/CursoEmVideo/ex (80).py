# peça 5 valores, na lista ja na posição certa sem usar o sort() ou sorted() e mostre a lista
# e mostrar a posição onde foi adicionado conforme é digitado, no fim mostrar lista
lista = []
for c in range(1,6):
    n = input(f'digite o valor {c} de 5: ')
    if c == 1:
        lista.append(n)
    if n > max(lista):
        lista.append(n)
        print(f'{n} foi inserido no fim da lista')
    if n < min(lista):
        lista.insert(0,n)
        print(f'{n} foi inserido no começo da lista')
print(lista)

