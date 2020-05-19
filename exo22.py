'''manipulacao de cadeia de caracteres string(str) '''

nome = str(input('Digite seu nome completo: ')).strip() #elemina os espaços
print('Analisando seu nome...')
print("Seu nome em maiusculas é {}".format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) #menos os espaços contados
print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) #mandei encontrar o primeiro espaco

