sal = float(input('digite o salário do funcionario para saber o aumento: R$ '))
aum = ''
if sal<1250:
    sal = sal + (sal*.15)
    aum = '15%'
else:
    sal = sal + (sal*.10)
    aum = '10%'
print('O novo salário é {} maior, ou seja, de R${:.2f}.'.format(aum, sal))