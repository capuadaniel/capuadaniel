g = str(input('Qual o seu sexo biologico?[M/F]')).upper().strip()
while g != 'M' and g != 'F':
    print('opção inválida')
    g = str(input('Qual o seu sexo biologico?[M/F]')).upper().strip()
    print(g)
print('Sexo biológico registrado como {}.'.format(g))

'''alternativamente'''

g = str(input('Qual o seu sexo biologico?[M/F/I]')).upper().strip()
while g not in 'MFI':
    print('opção inválida')
    g = str(input('Qual o seu sexo biologico?[M/F/I]')).upper().strip()
    print(g)
print('Sexo biológico registrado como {}.'.format(g))
