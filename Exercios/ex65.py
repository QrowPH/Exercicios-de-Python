n = c = s = maior = menor = media = 0
resp = 'S'
while resp == 'S':
    n = int(input('Digite um valor: '))
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    c += 1
    s += n
    media = s / c
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'A média dos valores é: {media:.2f}')
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')
