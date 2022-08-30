def spacify(string):
    res = ''
    for e in string:
        res += e + ' '

    if len(res) > 1:
        while res[-1] == ' ':
            res = res[:-1]
    return res


print(spacify('a'))
