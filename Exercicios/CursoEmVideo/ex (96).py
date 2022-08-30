#faça um programa com a 'função area' que receba altura e largura e calcule a área. mostre então as variaveis e a area calculada.
def area(h, w):
    print(f'Para a altura {h}m e a largura {w}m:')
    if h != w:
        print(f'A area do retangulo é <<< {h*w}m² >>>')
    else:
        print(f'A area do quadrado é <<< {h * w}m² >>>')

print('-='*20)
print('     Area do terreno     ')
print('-='*20)

recebea = float(input('Qual a altura do seu terreno? '))
recebel = float(input('Qual a largura do seu terreno? '))

area(recebea, recebel)