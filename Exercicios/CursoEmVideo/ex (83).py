#leia uma expressão matematica e verificar se os parenteses estão abertos e fechados na ordem correta. Use listas.
expressao = str(input('insira uma expressão matematica usando parenteses:'))
expressao_lis = expressao[:]
par_esq = par_dir = 0
for digito in expressao_lis:
    if digito == '(':
        par_esq += 1
    if digito == ')':
        par_dir += 1
print(par_esq)
print(par_dir)
if par_esq == par_dir:
    print('Esta expressão está correta')
else:
    print('Essa expressão contém erros')