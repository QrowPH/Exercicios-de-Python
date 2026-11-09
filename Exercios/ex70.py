total = caro = cont = menor = 0
barato = ''
while True:
    produto = str(input('Nome produto: ')).strip()
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        caro += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'O total da compra foi R${total:.2f}')
print(f'O total de compras acima de R$ 1000 foram {caro}')
print(f'O produto mais barato é {barato} e custa {menor:.2f}')
