casa = float(input('Qual valor da casa? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
parcelas = float(input('Quantos anos de financiamento? R$'))
prestaçao = casa / (parcelas * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos a prestaçao será de R${:.2f}'.format(casa, parcelas, prestaçao))
if prestaçao <= minimo:
    print('Empréstimo pode ser \033[32mCONCEDIDO\033[m!')
else:
    print('Empréstimo \033[31mNEGADO\033[m!')
