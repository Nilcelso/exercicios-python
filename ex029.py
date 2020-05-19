velocidade = float(input('Qual sua velocidade? '))
if velocidade > 80:
    print('MULTADO! Você excedeu a velocidade permitida que é de 80Km/h.')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de \033[31mR${:.2f}\033[m'.format(multa))
print('Tenha um bom dia! Dirija com segurança.')
