#faça a função escreva que recebe um parametro em texto e mostra linhas sobre e abaixo a frase acompanahndo o tamanho da frase.
def escreva(text):
    tamanho = len(text) + 4
    print('~'*tamanho)
    print(f'  {text}')
    print('~'*tamanho)


textos = list()
n_text = int(input('Quantos textos você quer fazer? '))
for n in range(0,n_text):
    textos.append(input(f'qual seu {n+1}º texto?'))

for n in textos:
    escreva(n)