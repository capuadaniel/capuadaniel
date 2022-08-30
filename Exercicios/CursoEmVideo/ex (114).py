#tesde se o site pudim está no ar e acessivel por esse computador
import urllib.request

try:
    urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('*'*12)
    print('pudim OFF')
else:
    print('*'*12)
    print('pudim ON')
finally:
    print('*'*12)
    print('faça pudim!')
    print('*'*12)
