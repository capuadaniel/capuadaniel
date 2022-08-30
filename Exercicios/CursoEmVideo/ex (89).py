#leia duas notas de alunos e guarde numa lsita composta no fim mostre o boletim de todos com nome e média, depois se o user digitar
# o numero do aluno mostrar as notas apenas daquele aluno/a.
aluno = []
lista = []
contador = especificar = 1

while True:
    aluno.append(str(input('Nome: ')).capitalize())
    aluno.append(float(input('nota 1: ')))
    aluno.append(float(input('nota 2: ')))
    aluno.append(float((aluno[1]+aluno[2])/2))
    aluno.append(int(contador))
    lista.append(aluno[:])
    aluno.clear()
    cont = input('continuar?[S/N]').strip()
    contador += 1
    if cont[0] in 'Nn':
        break

print('{:*^60}'.format(' BOLETIM '))
print('{:_^10} {:_<40} {:_^10}'.format('Nº','Nome','Média'))
for i in range(0,len(lista)):
    print('{:^10} {:<40} {:^10}'.format( lista[i][4], lista [i][0], lista[i][3] ))

while especificar != 0:
    especificar = int(input('Digite o numero do aluno para ver detalhes, ou 0 para fechar:'))
    if 0 < especificar < contador:
        for i in range(especificar-1, especificar):
            print('\n{:*^60}'.format(' BOLETIM de '+lista[i][0]+' '))
            print('{:_^10} {:_<20} {:_^10}{:_^10}{:_^10}'.format(' Nº', 'Nome', 'Nota 1 ', ' Nota 2 ', 'Média'))
            print('{:^10} {:<20} {:^10}{:^10}{:^10}'.format(lista[i][4], lista[i][0], lista[i][1], lista[i][2], lista[i][3]))
            break
print('FIM')
