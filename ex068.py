from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}')
    print('DEU PAR.' if total % 2 == 0 else 'DEU ÍMPAR.')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!!!')
            v += 1
        else:
            print('Você perdeu!!!')
            break
    if tipo == 'I':
        if total % 2 != 0:
            print('Você ganhou!!!!')
            v += 1
        else:
            print('Você perdeu!!!!')
            break
    print('Vamos jogar novamente....')
print(f'GAME OVER! Você venceu {v} vezes.')
