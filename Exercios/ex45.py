from random import randint
computador = randint(0, 2)
print("""Qual a sua jogada? 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jogador = int(input('Qual sua escolha: '))
if jogador == 0:
    if computador == 0:
        print('EMPATE!')
    elif computador == 1:
        print('PERDEU, BETINHA!')
    elif computador == 2:
        print('GANHOU, CALANGO!')
if jogador == 1:
    if computador == 0:
        print('GANHOU, CALANGO!')
    elif computador == 1:
        print('EMPATE!')
    elif computador == 2:
        print('PERDEU, BETINHA!')
if jogador == 2:
    if computador == 0:
        print('PERDEU, BETINHA!')
    elif computador == 1:
        print('GANHOU, CALANGO!')
    elif computador == 2:
        print('EMPATE')
else:
    print('ERRO OPÇÃO INVÁLIDA!')