import math
n = int(input('digite um numero'))
conv = float(input('''para qual base você quer converter esse numero:
(1)binário
(2)octal
(3)hexadecimal'''))

if conv == 1:
    print('\n',bin(n)[2:])
elif conv == 2:
    print('\n',oct(n)[2:])
elif conv == 3:
    print('\n',hex(n)[2:])
else:
    print('\nDigite uma opção de 1 a 3.')