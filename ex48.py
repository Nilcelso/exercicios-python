soma = 0
cont = 0
for impar in range(1, 501, 2):
    if impar % 3 == 0:
        cont = cont + 1
        soma = soma + impar
print('A soma de {} valores solicidados é {}.'.format(cont, soma))
