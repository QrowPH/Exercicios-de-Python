numeros = []
count = 0
while True:
    numeros.append(int(input('Digite um valor: ')))
    count += 1
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print(f'Você digitou {count} números!')
numeros.sort(reverse=True)
print(f'Os números digitados em ordem decrescente {numeros}')
if numeros.count(5):
    print(f'O número 5 está na lista')