palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
         'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
         'TRABALHAR', 'MERCADO', 'PROGRAMADOS', 'FUTURO','FELICIDADE','flor')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')