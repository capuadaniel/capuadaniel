#Crie um afunção fatorial() que receba 2 parametros, um é o numero o outro é um boleano que diz se o processo de fatorial será mostrado ou omitido
# essa função deve ter documentação.

def fatorial(n, show=False):
    """
    Mostra o fatorial de um numero e pode mostrar o processo de fatoramento ou não(padrão)
    :param n: numero a ser fatorado.
    :param show: 'True' para mostrar o processo 'False' para não mostrar.
    :return: retorna para o usuário um print com o numero fatorado, o processo de fatoração (opcional) e o resultado da fatoração.
    """
    f = 1
    for c in range(n,0,-1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

print(fatorial(4,True))
print(fatorial(4))
