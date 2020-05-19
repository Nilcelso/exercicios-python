resp = 'S'
media = quant = soma = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer contunuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} numeros e sua média é {}'.format(quant, media))
print('O maior nuúmero foi {} e o menor foi {}'.format(maior, menor))
print('ACABOU')
