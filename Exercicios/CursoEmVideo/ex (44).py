val = float(input("Valor da compra: "))

pag = str(input('''Digite a forma de pagamento:
(a) A vista, dinheiro ou cheque
(b) Débito ou Credito 1 x
(c) Crédito 2x
(d) Crédito 3x ou mais
'''))

if pag == 'a':
    val = val-(val*0.1)
elif pag == 'b':
    val = val - (val * 0.05)
elif pag == 'c':
    val = val
elif pag == 'd':
    val = val + (val * 0.2)

print('O valor da compra ficará R${:.2f}'.format(val))