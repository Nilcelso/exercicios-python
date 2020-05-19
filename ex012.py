pre = float(input('Qual o preço do seu produto? R$ '))
des = pre - (pre * 0.05)
print('O preço do produto é R$ {:.2f}, com 5% de desconto.'.format(des))