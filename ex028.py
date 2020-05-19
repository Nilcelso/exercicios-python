from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador escolher
print('--==--' * 10)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar....')
print('--==--' * 10)
jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar
print('PROCESSANDO.....')
sleep(4)
if jogador == computador:
    print('Parabéns!!! Você conseguiu me vencer, acertou que número pensei.')
else:
    print('Ganhei! Eu pensei no número {} e nao no {}.'.format(computador, jogador))
