import time

print('Fogos de artifício em 10 segundos!')

for contador in range (10,0,-1):
    print(contador,' ',end='')
    time.sleep(1)
print('')

for contador in range (4,0,-1):
    print('\033[31m {:^30}'.format('º*@*'*contador))
    print('{:^30}'.format('*#º@'*contador))
    print('{:^30}'.format('º *'*contador))
print('\033[34m{:^30}'.format('FELIZ ANO NOVO!'))