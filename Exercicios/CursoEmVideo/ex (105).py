def notas (*notas, sit=False):
    """
    Função que faz contas basicas sobre as contas de uma turma de alunos com notas de 0 a 10
    :param notas: qualquer quatidade de notas em inteiro ou float
    :param sit: parametro opcional 'situação' avaliando como boa uma média da turma >=7, razoavel >=5 e ruim abaixo de 5
    :return: retorna um dicionario com os valores calculados na ordem: total de notas, maior nota, menor nota, média e opcionalmente 'situação'.
    """
    t_notas = {}
    t_notas['total'] = len(notas)
    t_notas['maior'] = max(notas)
    t_notas['menor'] = min(notas)
    t_notas['média'] = sum(notas)/len(notas)
    if sit:
        if t_notas['média'] >= 7.5:
            t_notas['situação'] = 'boa'
        elif t_notas['média'] >= 5:
            t_notas['situação'] = 'razoável'
        else:
            t_notas['situação'] = 'ruim'
    return t_notas


turma1 = notas(3,4,5,6,7,8.5,9)
turma2 = notas(9,9,9,9,7,8.5,10)
turma3 = notas(3,4,2,2,3,1,1,1)
turma4 = notas(3,4,5,6,7,8.5,9, sit=True)
turma5 = notas(9,9,9,9,7,8.5,10, sit=True)
turma6 = notas(3,4,2,2,3,1,1,1, sit=True)

print(turma1)
print(turma2)
print(turma3)
print(turma4)
print(turma5)
print(turma6)
