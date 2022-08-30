from math import floor

def halving_sum(n):
    div = 2
    resp = n

    while floor(n/div) > 0:
        resp = floor(resp + n/div)
        div = div * 2
    return(resp)


print(halving_sum(25),'==> 47')