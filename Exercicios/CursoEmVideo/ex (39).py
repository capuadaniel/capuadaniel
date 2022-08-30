import datetime

ano = datetime.datetime.today().year
nasc = int(input('Em que ano você nasceu, jovem? \n'))
idade = ano-nasc

if idade < 18:
    print('Ainda faltam {} anos para o serviço militar obrigatório'.format(18-idade))
elif idade > 18:
    print('Você está {} anos atrasado para o serviço militar obrigatório'.format(idade-18))
else:
    print('Este ano vc deve se alistar no serviço militar obrigatório.')
