#cadastre uma lista com varios valores, se o numero for inédito adicione na lista, no fim mostre em ordem crescente.
n = '0'
lista = []
while n.isnumeric() == True:
    n = input('Adicione um numero (letra para encerrar): ')
    if n not in lista and n.isnumeric() == True:
        lista.append(int(n))
print(sorted(lista))