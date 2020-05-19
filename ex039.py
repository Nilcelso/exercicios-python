from datetime import date
atual = date.today().year
ano = int(input('Em que ano você nasceu? '))
idade =  atual - ano
print('Quam nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para alistamento.'.format(saldo))
    alistamento = atual + saldo
    print('Seu alistamento seá em {}'.format(alistamento))
elif idade > 18:
    saldo = idade - 18
    print('Você ja deveria ter se alistado há {} anos.'.format(saldo))
    alistamento = atual - saldo
    print('Seu alistamento foi em {}.'.format(alistamento))