números = (int(input('Digite um valor: ')),
           int(input('Digite um valor: ')),
           int(input('Digite um valor: ')),
           int(input('Digite um valor: ')))
print(f'Você digitou os valores {números}')
print(f'O número 9 apareceu {números.count(9)} vez')
if 3 in números:
    print(f'A posição do primeiro 3 é na {números.index(3)+1} posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
for n in números:
    if n % 2 == 0:
        print(n, end=' ')
