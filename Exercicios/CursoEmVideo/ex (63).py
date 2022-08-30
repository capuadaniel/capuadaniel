#mostre os n primeiros fibs
n = int(input('Quantos numeros da sequencia de fibonacci vc quer? '))
t1 = 0
t2 = 1
n -= 2
print(t1,  t2, end=' ')

while n > 0:
    t3 = t1 +t2
    t1 =t2
    t2 = t3
    print('{} '.format(t3), end='')
    n -= 1
'''
while n > 0:
    t1 = t1+t2
    n -= 1
    print(t1, end=' ')
while n > 0:
    t2 = t1+t2
    n -= 1
    print(t2, end=' ')
'''