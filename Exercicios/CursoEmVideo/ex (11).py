b = float(input('qual a base da parede?\n'))
a = float(input('qual a altura da parede?\n'))
area = b*a
litros = area/2
print('você precisa de {}L de tinta para pintar essa parede.'.format(litros))