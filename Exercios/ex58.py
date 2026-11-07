from random import randint
computador = randint(0, 10)
print('Vou pensar em um número entre 0 e 10')
print('Você consegui advinhar?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('MAIS...')
        if jogador > computador:
            print('MENOS...')
print(f'ACERTOU! SEU MERDINHA, DEMOROU ISSO PRA ACERTAR! {palpite}')
