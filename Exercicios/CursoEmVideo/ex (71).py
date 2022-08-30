#caixa eletronico, pergunte o valor sacado (int) e o programa dá as cedulas 50 20 10 1

print('''
----------------------------
|                           |
|   QUANTO VC QUER SACAR?   |
|                           |
|                           |
|   _____________________   |
|  |                     |  |
|  |   $  $    $  $   $  |  |
|    $   $  $   $   $   $   |
|   _____________________   |
''')

valor_sacado = int(input('R$ '))

cinq = valor_sacado // 50
valor_sacado = valor_sacado - (cinq * 50)
print(valor_sacado)

vint = valor_sacado // 20
valor_sacado = valor_sacado - (vint * 20)
dez = valor_sacado // 10
valor_sacado = valor_sacado - (dez * 10)
um = valor_sacado // 1


print(f'''O caixa entregou
{cinq} notas de R$50,00
{vint} notas de R$20,00
{dez} notas de R$10,00
{um} notas de R$1,00''')
