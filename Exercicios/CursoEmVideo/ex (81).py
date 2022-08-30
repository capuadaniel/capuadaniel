#leia varios e mostre a-quantos n digitados, b- lista desc, e se 5 foi digitado e está na lista
lista = []
while True:
    n = input('Digite um valor: ')
    if n.isnumeric() == True:
        lista.append(int(n))
    if n.isnumeric() == False:
        break
print(f'Foram digitados {len(lista)} números.')
print(f'Os valores do maior para o menor são foram: \n {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 foi digitado.')
else:
    print('O valor 5 não foi digitado nenhuma vez.')