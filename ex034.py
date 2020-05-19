salario = float(input('Qual o salário do funcionário? R$'))
if salario <= 1250:
    novo = salario + (salario * 0.15)
else:
    novo = salario + (salario * 0.10)
print('O novo salário do funcionário é \033[32mR${:.2f}.'.format(novo))