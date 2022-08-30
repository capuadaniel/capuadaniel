#20 numeros por extenso
ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desesseis', 'desessete', 'dezoito', 'desenove', 'vinte')
n = int(input('digite um numero de 0 a 20: '))
while n < 0 or n > 20:
    n = int(input('tente novamente, digite um numero de 0 a 20: '))
print(f'Você digitou o numero {ext[n]}.')