n = int(input('quer saber a tabuada de qual numero? '))
for inc in range(1,11):
    print('{:^2} x {:^2} = {:^2}'.format(n, inc, n*inc))