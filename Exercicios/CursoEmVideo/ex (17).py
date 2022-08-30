import math
c = float(input('Digite um cateto de seu triangulo retangulo: '))
h = float(input('Agora digite o outro cateto: '))
hipotenusa = math.hypot(c , h)
print('A hipotenusa desse triangulo é:{}'.format(hipotenusa))
