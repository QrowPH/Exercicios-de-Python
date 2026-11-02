salário = float(input('Digite seu salário: R$ '))
if salário <= 1621:
    novo = salário + (salário * 15 / 100)
    print(f'Seu salário de R${salário}, seu novo salário é R${novo}')
else:
    novo = salário + (salário * 10 / 100)
    print(f'Seu salário de R${salário}, seu novo salário é R${novo}')