#mirim 9 infantil 14 junior 19 senior 20 master >
import datetime
nasc = int(input('ano nasc do atleta:'))
ano = datetime.datetime.today().year
idade = ano - nasc

if idade <= 9:
    print('classificação:Mirim')
elif idade <= 14:
    print('classificação:Infantil')
elif idade <= 19:
    print('classificação:Junior')
elif idade <= 25:
    print('classificação:Senior')
else:
    print('classificação:Master')

print (idade)