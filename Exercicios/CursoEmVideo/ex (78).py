# leia 5 valores e guarde na lista, mostre o maior eo menor e suas posições
# (se o numero se repete deve mostrar todas as posições em que apareceu
lista=[]
#fazendo a lista
for c in range(0,5):
    n = input('Digite um numero para a lista ou uma letra para terminar: ')
    lista.append(n)

#achando as posições
max = max(lista)
max_pos =[]
for p, c in enumerate(lista):
    if c == max:
        max_pos.append(p)
min = min(lista)
min_pos =[]
for p, c in enumerate(lista):
    if c == min:
        min_pos.append(p)
#========resultado=======
print('*'*60)
print(f'Lista:{lista}')
if len(max_pos) > 1:
    print(f'O maior valor é {max} nas posições:{max_pos}')
else:
    print(f'O maior valor é {max} na posição:{max_pos}')
if len(min_pos) > 1:
    print(f'O menor valor é {min} nas posições:{min_pos}')
else:
    print(f'O menor valor é {min} na posição:{min_pos}')
