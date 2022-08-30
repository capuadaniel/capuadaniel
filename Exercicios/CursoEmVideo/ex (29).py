vel = float(input('qual velocidade (Km/h) desse carro que passou? '))
if vel>80:
    multa = (vel - 80) * 7
    print('Estava acima do limite, a multa é R${:.2f}.'.format(multa))
else:
    print ('Estava na velocidade permitida.')
