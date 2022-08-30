n = 0
while True:
    n = int(input('Quer a tabuada de qual numero?'))
    if n < 0:
        break
    for c in range(1,11,1):
        print(f'{n} x {c} = {n*c}')
