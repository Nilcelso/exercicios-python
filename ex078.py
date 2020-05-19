listanum = []
maior = 0
menor = 0
for c in range (0, 5):
    listanum.append(int(input(f'Digite um valor para a posiçáo {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} nas posiçóes ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end=' ')
print(f'\nO menor valor digitado foi {menor} nas posiçóes ', end='')
for g, d in enumerate(listanum):
    if d == menor:
        print(f'{g}....', end=' ')
