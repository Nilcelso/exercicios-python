print('-=-' * 9)
print('\033[7;37;46mAnalisador de triângulos.\033[m')
print('-=-' * 9)
a: float = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < c + a and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triângulo')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')