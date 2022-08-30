import math
ang = float(input('digite um angulo em graus: '))
ang = math.radians(ang)
sen = math.sin(ang)
cos = math.cos(ang)
tan = math.tan(ang)
print('para esse angulo estes são os valores de \nseno {:.2} \ncoseno {:.2} \ntangente {:.2}'.format(sen, cos, tan))