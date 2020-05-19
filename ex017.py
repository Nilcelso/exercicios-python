'''importando biblioteca (import) math e random e importar do site python.org'''

'''fazendo o calculo da hipotenusa usando as bibliotecas'''
import math
co = float(input('Comprimento de um dos catetos: '))
ca = float(input('Comprimento do outro cateto: '))
hi = math.hypot(ca, co)
print('O valor da hipotenusa é: {:.2f}'.format(hi))

'''
from math import hypot
co = float(input('Comprimento de um dos catetos: '))
ca = float(input('Comprimento do outro cateto: '))
hi = math.hypot(ca, co)
print('O valor da hipotenusa é: {:.2f}'.format(hi))

'''

'''fazendo matematicamente o calculo da hipotenusa'''
'''co = float(input('Comprimento do cateto oposto:  '))
ca = float(input('Comprimento do cateto oposto: '))
hip = (ca**2 + co**2) ** (1/2)
print('O valor da hipotenusa é: {}'.format(hip))'''
