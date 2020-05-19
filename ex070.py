print('-=-=-='*10)
print('{:^50}'.format('LOJA O BARATÃO'))
print('-=-=-='*10)
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Qual o produto? '))
    preco = float(input('Preçp: R$'))
    cont +=1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer contunuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'O total da compra foi de R${total:.2f}.')
print(f'Temos {totmil} produtos custando mais de R$1000,00')
print(f'O produto mais barato custa R${menor:.2f} e é o {barato}')
print('{:-^40}'.format('FIM DO PRPGRAMA.'))
