print('Fatorial')
n = int(input('digite um numero: '))
c = n
fatW = 1
fatF = 1

# ===================================
while c > 0:
    fatW *= c
    c = c -1

# ===================================
for c in range(n, 1, -1):
    fatF *= c

print('Com While o fatorial é: {}.'.format(fatW))
print('Com For o fatorial é: {}.'.format(fatF))
