nome = input('Digite seu nome completo cidadã(o): ').strip()
nomao = nome.upper()
nominho = nome.lower()
semespaco = len(nome.replace(' ',''))
nomeletras = len(nome.split()[0])

print('Seu nomão é {}.'.format(nomao))
print('Seu nomminho é {}.'.format(nominho))
print('Seunomesemespaçotem{}letras.'.format(semespaco))
print('E seu primeiro nome tem {} letras.'.format(nomeletras))

#alternativamente

print('\nAlternativamente:\nseu nome tem {} letras'.format(len(nome)-nome.count(' ')))
print('e seu primeiro nome tem {} letras'.format(nome.find(' ')))