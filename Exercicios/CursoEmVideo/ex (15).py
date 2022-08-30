dias = float(input('quantos dias o carro ficou alugado?'))
km = float(input('quantos km o carro rodou?'))
retorica = float(input('quanto você quer pagar?'))
preço_dia = dias * 60
preço_km = km*0.15
soma= preço_dia+preço_km
print('errou, não vai pagar R${:.2f}, não.'.format(retorica))
print('o aluguel saiu por R$ {:.2f} (dias de uso) + R$ {:.2f} (quilometragem rodada), totalizando R$ {:.2f}.'.format(preço_dia, preço_km, soma))
print('\npensou que ia pagar {} e vai pagar {}.' .format(retorica, soma))