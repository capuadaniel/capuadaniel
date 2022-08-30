def powers_of_two(n):
    lista = []
    power = 0
    for c in range (0, n+1):
        n_lista = 2 ** abs(power)
        power += 1
        lista.append(n_lista)
    return lista

print(powers_of_two(0), 'power 0')
print(powers_of_two(1), 'power 1')
print(powers_of_two(2), 'power 2')
print(powers_of_two(4), 'power 4')