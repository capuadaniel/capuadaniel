def remainder(a,b):
    maior = max(a, b)
    menor = min(a, b)
    if menor == 0:
        return None
    else:
        return maior % menor


print(remainder(17, 5),'Returned value should be the value left over after dividing as much as possible.')
print(remainder(13, 72), 'The order the arguments are passed should not matter.')
print(remainder(1, 0),'Divide by zero should return None')
print(remainder(0, 0), 'Divide by zero should return None')
print(remainder(0, 1), 'Divide by zero should return None')
print(remainder(-1, 0), 'Divide by zero should only be checked for the lowest number')
print(remainder(0, -1), 'Divide by zero should only be checked for the lowest number')
print(remainder(-13, -13), 'Should handle negative numbers')
print(remainder(-60, 340),  'Should handle negative numbers')
print(remainder(60, -40), 'Should handle negative numbers')