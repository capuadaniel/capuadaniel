frase = str(input('digite uma frase para descobrir se é palindromo:\n ')).strip().lower()
frase = frase.replace(' ', '')
ultimo = len(frase)
conta = 1
p = 0
for c in range(0, (len(frase)//2)):
    if frase[-1+conta] == frase[ultimo-conta]:
        p = p+0
    else:
        p = p+1
    conta = conta + 1

if p == 0:
    print(' *'*10,'\n  É palindromo!\n','* '*10)
else:
    print(' *'*10,'\n  Não é palindromo!\n','* '*10)
