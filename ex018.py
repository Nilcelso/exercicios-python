'''import math
ang = float(input('Digite um angulo: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print('O angulo de {} tem seno de {:.2f}'.format(ang, seno))
print('O angulo de {} tem cosseno de {:.2f}'.format(ang, cosseno))
print('O angulo de {} tem tangente de {:.2f}'.format(ang, tangente))'''


from math import radians, sin, cos, tan
ang = float(input('Digite um angulo: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print('O angulo de {} tem seno de {:.2f}'.format(ang, seno))
print('O angulo de {} tem cosseno de {:.2f}'.format(ang, cosseno))
print('O angulo de {} tem tangente de {:.2f}'.format(ang, tangente))

''' qualquer um dos dois estao rodando '''