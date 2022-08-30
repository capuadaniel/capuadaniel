def sum_mul(n, m):
    if m <= 0 or n <= 0:
        return "INVALID"
    else:
        lista = []
        for num in range (0,m,n):
            if num != 0:
                lista.append(num)
        print (lista)
        soma = sum(lista)
    return soma


print(sum_mul(0, 0), 'INVALID')
print('-'*90)
print(sum_mul(0, 2), 'INVALID')
print('-'*90)
print(sum_mul(2, 9), '==>20')
print('-'*90)
print(sum_mul(3, 13), '==>30')
print('-'*90)
print(sum_mul(4, 123), '==>1860')
print('-'*90)
print(sum_mul(4, -7), 'INVALID')