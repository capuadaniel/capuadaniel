def moeda(n, moeda):
    n = (f'{n:.2f}')
    return f'{moeda}{n}'.replace('.',',')


def aumentar(n, p, dinheiro=False):
    n += n*(p/100)
    if dinheiro == True:
        return moeda(n)
    else:
        return n

def diminuir(n, p, dinheiro=False):
    n -= n*(p/100)
    if dinheiro == True:
        return moeda(n)
    else:
        return n


def dobro(n, dinheiro=False):
    n = n*2
    if dinheiro == True:
        return moeda(n)
    else:
        return n


def metade(n, dinheiro=False):
    n = n/2
    if dinheiro == True:
        return moeda(n)
    else:
        return n

def resumo(n, aum=00, dim=00):
    print('----------------------------------')
    print(' = = = = Resumo do valor  = = = = ')
    print('----------------------------------')

    print(f'{"Preço analisado:":<24}\t{moeda(n)}')
    print(f'{"Dobro do preço:":<24}\t{dobro(n, True)}')
    print(f'{"Metade do preço:":<24}\t{metade(n, True)}')

    print(f'{str(aum)+"% de aumento":<24}\t{aumentar(n, aum, True)}')
    print(f'{str(dim)+"% de diminição":<24}\t{diminuir(n, dim, True)}')

    print('----------------------------------')
