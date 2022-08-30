def cabecalho(texto, larg = 50):
    print('*'* larg)
    print(texto.center(larg))
    print('*'* larg)

def menu (*itens):
    contador = 1
    for elementos in itens:
        print(f'{contador} - \033[34m{elementos}\033[m')
        contador += 1


def existearquivo(nome):
    try:
        arq = open(nome, 'rt')
        arq.close()
    except (FileNotFoundError):
        print('\033[31m Arquivo de registro criado! \033[m')
        return False
    except:
        return False
    else:
        return True

def criaarquivo(nome):
    try:
        open(nome, 'wt+')
    except:
        print("Erro ao criar arquivo, verificar ex115_modulo def criaarquivo()")

def cadastrar(arquivo, nome,idade):
    try:
        arq = open(arquivo, 'at+')
    except:
        print('erro ao cadastrar')
    else:
        arq.write(f"{nome};{idade}\n")
        print(f'\033[42m{nome}, {idade} anos -> CADASTRADO COM SUCESSO.\033[m')
    finally:
        arq.close()

def lerCadastro(nome):
    try:
        arq = open(nome, 'rt')
    except FileNotFoundError:
        print('Erro ao ler o aquivo//lerCadastro()')
    else:
        cabecalho("CADASTRO")
        for linhas in arq:
            dado = linhas.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'\033[34m{dado[0]:<40}{dado[1]:>10} anos\033[m')
        print(arq.read())