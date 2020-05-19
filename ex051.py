num = int(input('Digite um número: '))
r = int(input('Razao: '))
decimo = num + (10 - 1) * r
for pa in range (num, decimo + r, r):
   print('{} '.format(pa), end=' -> ')
print(' ACABOU!!')