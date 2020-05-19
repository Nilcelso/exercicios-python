n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('A media do aluno foi {:.2f}, Ele está \033[31mREPROVADO\033[m.'.format(media))
elif media >= 5 and media < 7:
    print('A media do aluno foi {:.2f}. Ele está de \033[32mRECUPERAÇÃO\033[m.'.format(media))
else:
    print('A media do aluno foi {:.2f}. Ele está \033[34mAPROVADO\033[m.'.format(media))
