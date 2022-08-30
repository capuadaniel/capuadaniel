'''n = ''
while len(n) != 9:
    n= input('insira os 9 valores para uma matriz 3x3 separados por espaço: \n').split()

matriz = [ [ n[0],n[1],n[2] ],[ n[3],n[4],n[5] ],[ n[6],n[7],n[8] ] ]

print('[{:^5}]  [{:^5}]  [{:^5}]'.format(matriz[0][0],matriz[0][1],matriz[0][2]))
print('[{:^5}]  [{:^5}]  [{:^5}]'.format(matriz[1][0],matriz[1][1],matriz[1][2]))
print('[{:^5}]  [{:^5}]  [{:^5}]'.format(matriz[2][0],matriz[2][1],matriz[2][2]))
'''
#<<<<<<<<<<<< alternativamente >>>>>>>>>>>>>>>>>>>

matriz = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f'digite o valor para a posição {i+1}x{j+1}: '))
for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]:^10}]', end='')
    print('')
