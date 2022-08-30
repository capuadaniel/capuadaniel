#leia nome, ano de nasc e ctps(carteira de trabalho), cadastre os dados com a idade no lugar do ano de nasc num dicio e
#se o ctps for diferente de zero cadastre também o ano de contratação eo salário, calcule e acrescente ao dicio com quantos
#anos a pessoa vai se aposentar (consderando 35 anos de contribuição)
import datetime as dt
ano_cont = salario = ctps = apo_ano = ''
cidadao = {}
cidadao['nome']= input('Nome: ')
cidadao['idade'] = dt.datetime.today().year - int(input('Ano de Nasc: '))

cidadao['ctps'] = input('N da carteira de trabalho (vazio pula): ')
if cidadao['ctps'].isnumeric() == True:
    cidadao['ano_cont'] = input('Ano de contratação: ')
    cidadao['salario'] = float(input('Primeiro Salário: '))
cidadao['apo_ano'] = cidadao['idade'] + 35

print(cidadao)

if cidadao['ctps'] != '':
    print('=*'*20, 'REGISTRO', '*='*20)
    for k, v in cidadao.items():
        print(f'{k} : {v}')
else:
    cont = 1
    print('=*'*20, 'REGISTRO', '*='*20)
    for k, v in cidadao.items():
        print(f'{k} é {v}')
        cont += 1
        if cont == 3:
            break