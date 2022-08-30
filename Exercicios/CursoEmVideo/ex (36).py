valcasa = float(input('Qual o valor da casa que você quer financiar? '))
valsal = float(input('Qual seu salario? '))
qtsanos = int(input('Em quantos anos você quer financiar essa casa?'))
samwilson = str(input('Você se chama Sam Wilson? Sim/Não')).lower()

print(samwilson)
if samwilson == 'sim':
    print('Seu emprestimo está aprovado!')
else:
    crivo = valsal*.3
    prestacao = valcasa / (qtsanos * 12)
    if prestacao>crivo:
        print('Você não pode financiar esse imóvel.')
    else:
        print('Seu emprestimo está aprovado, suas mensalidades serão de R${.:2f}.'.format(prestacao))