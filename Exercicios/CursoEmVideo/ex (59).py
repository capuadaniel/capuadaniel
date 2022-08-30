#leia dois valores soma multiplica maior novos n ou sair
print('-*'*20)
print('Digite dois numeros!')
print('-*'*20)
a = float(input('n1: '))
b = float(input('n1: '))
c = 'rodou'
while c != 'parou':
    opt = float(input('''Você gostaria de:
    [1]Somar
    [2]Multiplicar
    [3]Saber o maior
    [4]Trocar os numeros
    [5]Sair
    Sua opção: '''))
    print(' ')
    if opt == 1:
        print('a soma de {} e {} é {}.'.format(a, b , a+b))
    elif opt == 2:
        print('a multiplicação de {} por {} é {}.'.format(a, b, a*b))
    elif opt == 3:
        if b > a:
            print('{} é maior que {}'.format(b, a))
        else:
            print('{} é maior que {}'.format(a, b))
    elif opt == 4:
        a = float(input('n1: '))
        b = float(input('n1: '))
    elif opt == 5:
        print('FIM')
        c = 'parou'
    else:
        print('Opção invalida, digite uma opção entre 1 e 5')