n = str(input('Qual seu nome completo? ')).strip().upper()
nome = n.split()
print('Prazer em te conhecer, {}'.format(nome[0]))
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu ultimo nome é: {}'.format(nome[len(nome)-1]))

