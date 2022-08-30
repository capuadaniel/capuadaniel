#Crie leiaInt() que funciona como input, mas só funciona com int e ao receber algo não numerico retorna erro.
def leiaInt(n):
    while True:
        if str(n).isnumeric() == False:
            print(f'<<<Erro, n tem que ser Inteiro.>>>')
            n = input('Digite um numero inteiro: ')
        else:
            return n

n = input('Digite um numero inteiro: ')
print(f'   -> Você digitou o numero {leiaInt(n)}.')
