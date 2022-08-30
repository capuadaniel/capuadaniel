ano = int(input('Em que ano estamos? '))

div4 = ano % 4
div100 = ano % 100
div400 = ano % 400

print(div4, div100, div400)

# ou if div4 == 0 and div100 != 0 or div400 == 0
if div4 == 0:
    if div100 != 0:
        if div400 == 0:
            print('{} é bisexto'.format(ano))
        else:
            print('{} não é bisexto'.format(ano))
    else:
        print('{} não é bisexto'.format(ano))
else:
    print('{} não é bisexto'.format(ano))