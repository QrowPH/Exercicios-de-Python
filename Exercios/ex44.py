produto = float(input('Qual o preço do produto? R$ '))
print("""Condição de pagamento:
[ 1 ] Á vista dinheiro/cheque
[ 2 ] Á vista no cartão
[ 3 ] Parcelado 2x sem juros
[ 4 ] Parcelado 3x ou mais com juros""")
opção = int(input('Qual a forma de pagamento? '))
if opção == 1:
    total = produto - (produto * 10 / 100)
elif opção == 2:
    total = produto - (produto * 5 / 100)
elif opção == 3:
    total = produto
    parcela = total / 2
    print(f'Sua compra vai ser parcelada em 2x de R$ {parcela:.2f} SEM JUROS!')
elif opção == 4:
    total = produto + (produto * 20 / 100)
    totalparc = int(input('Quantos parcelas? '))
    parcela = total / totalparc
    print(f'Sua compra será parcelada em {totalparc}x de R$ {parcela:.2f}')
else:
    total = produto
    print('OPÇÂO INVÁLIDA de pagamento! tente novamente!')
print(f'Sua compra foi de R${produto:.2f} vai custar R${total:.2f}')
