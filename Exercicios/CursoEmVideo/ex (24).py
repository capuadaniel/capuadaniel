cidade = input('digite sua cidade: ').strip()
cidade = cidade.upper()
cidade = cidade.split()

resultado = 'SANTO' in cidade[0]

print(
'''    Esse programa é muito util e vai te dar 
    uma informação valiosa que você, imbecil, 
    não sabia:
    
    Sua cidade começa com Santo?: {}'''.format(resultado)
)