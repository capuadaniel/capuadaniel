def to_alternating_case(string):
    letrocada = ''
    for letra in string:
        if letra.islower() == False:
            letrocada += letra.lower()
        else:
            letrocada += letra.upper()
    return letrocada

print(to_alternating_case('DaNiEl'))