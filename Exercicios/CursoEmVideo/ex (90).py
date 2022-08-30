#leia o nome e a média de um aluno e guarde também a situação em um dicionario, no fim mostre uma tabela com todas info (média 7 ou mais está aprovado)
aluno={}

aluno['nome'] = str(input('NOME: '))
aluno['media'] = float(input('MÉDIA: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'
else:
    aluno['situacao'] = 'reprovado'

print('*'*30)
for k, v in aluno.items():
    print(f'{k} é {v}')