from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opçao = 0
while opçao !=5:
    print('''    [ 1 ] SOMAR
    [ 2 ] MUTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NUMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opçao = int(input('>>>>>>>> Qual a sua opção? '))
    if opçao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1, n2, soma))
    elif opçao == 2:
        mult = n1 * n2
        print('A multimplicaçao entre {} e {} é {}'.format(n1, n2, mult))
    elif opçao == 3:
        if n1 > n2:
            print('O maior numero entre {} e {} é {}.'.format(n1, n2, n1))
        elif n2 > n1:
            print('O maior numero entre {} e {} é {}.'.format(n1, n2, n2))
        else:
            print('Os numeros digitados são iguais.')
    elif opçao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opçao == 5:
        print('finalizando.....')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Vote sempre!')
