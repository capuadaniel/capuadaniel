print('-'*15)
print('\033[1;32m Leitor de IMC\033[m')
print('-'*15)

peso = float(input('Peso (kg): '))
altura = float(input('Altura (m): '))
IMC = peso / altura**2
print('seu IMC é {:.2f}.'.format(IMC))
if IMC <= 18.5:
    print('abaixo do peso')
elif IMC <= 25:
    print('peso ideal')
elif IMC <= 30:
    print('sobrepeso')
elif IMC <= 40:
    print('obesidade')
else:
    print('obesidade mórbida')
