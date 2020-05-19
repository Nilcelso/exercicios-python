larg = float(input('Qual a largura da sua parede? '))
alt = float(input('Qual a altura da sua parede? '))
a = larg * alt
tinta = a/2
print('Sua parede tem a dimensão de {:.2f} x {:.2f} e sua área é de {:.2f} metros quadrados.'.format(larg, alt, a))
print('Para pintar essa parede vc precisa de {:.2f}L de tinta'.format(tinta))
