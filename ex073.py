times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
         'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará',
         'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
for t in times:
    print(f'{t}')
print(f'Os cinco primeiros são: {times[0:5]}')
print(f'Os quatro ultimos sao: {times[-4:]}')
print(f'times em ordem alfabetica: {sorted(times)}')
print(f'O chapecoense está na {times.index("Chapecoense") + 1}ª posição.')
