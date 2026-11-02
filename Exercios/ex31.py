viagem = int(input('De quantos Km é sua viagem? '))
passagem = viagem * 0.50
if viagem <= 200:
    print(f'Sua viagem vai custar R${passagem}')
else:
    passagem = viagem * 0.45
    print(f'Sua viagem vai custar R${passagem}')