def amount_of_pages(summary):
    list = []
    test = ''
    ultimo = 0
    for n in range(1,summary+1):
        list.append(n)

    for e in list:
        if len(test) < int(summary):
            test += str(e)
            ultimo = e

        else:
            break

    return ultimo

print(amount_of_pages(25))