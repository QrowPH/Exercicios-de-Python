from random import randint
from time import sleep
computador = randint(0, 5)
print('Pensei em um número entre 0 e 5')
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
if jogador == computador:
    print('Você venceu!')
else:
    print('Você perdeu! seu betinha')