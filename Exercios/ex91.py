from random import randint
from time import sleep
from operator import itemgetter
jogos = {'Jogador 1':randint(1,10),'Jogador 2': randint(1,10),
           'Jogador 3': randint(1,10),'Jogador 4': randint(1,10)}
ranking = list()
print('Valores sorteados:')
for k, v in jogos.items():
    print(f'O {k} tirou {v}')
    sleep(1)
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print('-=' * 10)
print(f'{"Ranking":^20}')
print('-=' * 10)
for i, v in enumerate(ranking):
    print(f'{i+1} Lugar: {v[0]} com {v[1]}')
    sleep(1)