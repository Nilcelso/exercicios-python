d = float(input('Quanto você tem na carteira? R$ '))
dolar = d/3.27
euro = d/4.68
iene = d/0.039
print('Com R${:.2f} você pode comprar: \n{:.2f} Dólares\n{:.2f} Euros\n{:.2f} Ienes'.format(d, dolar, euro, iene))
