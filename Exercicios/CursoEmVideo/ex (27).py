nome = input('digite seu nome completo: ')
nome = nome.title()
nome = nome.split()
comp = len(nome)

primeiro = nome[0]
ultimo = nome[comp-1]
print('primeiro nome: ',primeiro)
print('primeiro nome: ',ultimo)