from random import randint
números = (randint(1,10), randint(1,10), randint(1,10),
           randint(1, 10), randint(1,10))
maior = menor = cont = 0
for c in números:
    cont += 1
    if cont == 1:
        maior = menor = c
    else:
        if c > maior:
            maior = c
        if c < menor:
            menor = c
    print(f'{c} ', end='')
print()
print(f'O maior número sorteado foi {maior}')
print(f'O menor número sorteado foi {menor}')
