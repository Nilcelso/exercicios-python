print('-=-' * 9)
print('\033[33;46mCaucule o seu IMC.\033[m')
print('-=-' * 9)
peso = float(input('Qual seu peso: (KG) '))
altura = float(input('Qual sua altura: (m) '))
imc = peso / (altura ** 2)
print("O IMC dessa pessoa é de {:.2f}".format(imc))
if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobre peso.')
elif 30 <= imc < 40:
    print('Obesidade.')
else:
    print('Obesidade morbida.')
