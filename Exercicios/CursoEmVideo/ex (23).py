numerodequatrodigitos = str(input('Escreva um numero de até 4 digitos: '))

zeros = "0000"

numerojunto = zeros+numerodequatrodigitos
comprimento = len(numerojunto)

u = numerojunto[comprimento-1]
d =  numerojunto[comprimento-2]
c =  numerojunto[comprimento-3]
m =  numerojunto[comprimento-4]

print(
    '''
Você digitou {}. Este numero contém:

unidades:{}
dezenas:{}
centenas:{}
milhares:{}
''' .format(numerodequatrodigitos, u, d, c ,m)
)