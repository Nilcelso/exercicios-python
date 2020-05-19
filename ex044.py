print('{:=^40}'.format(' MODA NILCELSO '))
preco = float(input('Preço das compras: R$ '))
print(''' FORMAS DE PAGAMENTO
[ 1 ] À VISTA NO DINHEIRO/CHEQUE
[ 2 ] À VSITA NO CARTÃO
[ 3 ] 2X NO CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO''')
opcao = int(input('Qual é a forma de pagamento? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparcela = int(input('Quantas parcelas? '))
    parcela = total / totalparcela
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(totalparcela, parcela))
else:
    total = 0
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente.')
print('Sua compra de R${:.2f} sai por R${:.2f} no final'.format(preco, total))
print('\033[7;33m{:=^60}\033[m'.format(' A MODA NILCELSO AGRADECE A PREFERENCIA '))
