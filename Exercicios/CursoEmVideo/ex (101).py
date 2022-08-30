#crie a F voto() e receba o ano de nascimento de uma pessoa retornando uma frase dizendo se o voto dela é obrigatório, opcional ou proibido
# a saida deve ser "com x anos o voto é y".
from datetime import datetime

def voto(anonasc):
    hoje = datetime.today().year
    anoaval = abs(anonasc - hoje)
    if anoaval <16:
        print(f'Com {anoaval} anos o voto é Proibido')
    elif anoaval <18 or anoaval >= 65:
        print(f'Com {anoaval} anos o voto é Opcional')
    elif anoaval >= 18 and anoaval < 65:
      print(f'Com {anoaval} anos o voto é Obrigatório')

for n in range(1950,2021):
    voto(n)
