#Aprimore o anterior e mostre a soma dos valores, a soma da terceira coluna, o maior da segunda linha.
somapares = soma3col = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f'digite o valor para a posição {i+1}x{j+1}: '))
for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]:^10}]', end='')
        if matriz[i][j] % 2 == 0:
            somapares += int(matriz[i][j])
    soma3col += int(matriz[i][2])
    print('')
maior2linha = max(matriz[1])
print(f'A soma dos pares é: {somapares}')
print(f'A soma da terceira coluna é: {soma3col}')
print(f'O maior da segunda linha é: {maior2linha}')
