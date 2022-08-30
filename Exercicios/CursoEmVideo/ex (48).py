#1 500 3 em 3 soma impares
s = 0
for c in range(3,501,3):
    if c % 2 != 0:
        s = s +c
print(s)