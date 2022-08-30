import datetime
anoatual = datetime.date.today().year
tot_maior = 0
tot_menor = 0

for c in range(0,7):
    anonasc = int(input('ano de nascimento: '))
    if anoatual - anonasc <18:
        tot_maior += 1
        print('é menor de idade.')
    else:
        tot_menor += 1
        print('é maior de idade.')
print('{} pessoas são maiores de idade e {} são menores.'.format(tot_maior, tot_menor))