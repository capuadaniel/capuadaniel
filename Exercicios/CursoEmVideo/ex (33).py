num = str(input('escreva 3 numeros separados por espaço: ')).split()
a = float(num[0])
b = float(num[1])
c = float(num[2])

if a > b and a > c:
    print("{} é o maior numero".format(a))
if b > a and b > c:
    print("{} é o maior numero".format(b))
if c > a and c > b:
    print("{} é o maior numero".format(c))

if a < b and a < c:
    print("{} é o menor numero".format(a))
if b < a and b < c:
    print("{} é o menor numero".format(b))
if c < a and c < b:
    print("{} é o menor numero".format(c))
