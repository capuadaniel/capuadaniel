maiores_de_idade = homens = mulheres_menores = 0

print('====CADASTRO====')
while True:
    print('-'*30)
    idade = ' '
    while idade.isnumeric() == False:
        idade = str(input('Idade em anos: '))
    genero = ' '
    while genero not in 'mif':
        genero = str(input('Genero[M/I/F]: ')).lower().strip()[0]
    cadastro = ' '
    while cadastro not in 'sn':
        cadastro = str(input('Continuar cadastrando?[S/N]')).lower().strip()[0]

    if int(idade) >= 18:
        maiores_de_idade += 1
    if genero == 'm':
        homens += 1
    if int(idade) < 20 and genero == 'f':
        mulheres_menores += 1
    if cadastro == 'n':
        break

print(f'''\nDos cadastrados sabe-se que:
{maiores_de_idade} são maiores de idade,
{homens} são homens e,
{mulheres_menores} são mulheres de menos de 20 anos.''')
