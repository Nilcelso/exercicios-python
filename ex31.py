'''distancia = float(input('Qual é ditância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}km'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.5
    print('Sua viagem custará R${:.2f}.'.format(preco))
else:
    preco2 = distancia * 0.45
    print('Sua viagem custará R${:.2f}.'.format(preco2))'''


distancia = float(input('Qual é ditância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}km'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
print('Sua viagem custará R${:.2f}.'.format(preco))
