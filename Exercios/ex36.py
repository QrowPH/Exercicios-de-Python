valor = int(input('Qual o valor da casa? '))
salário = float(input('Qual o seu salário? '))
ano = int(input('Em quantos anos você quer pagar a casa? '))
parcela = valor / (ano * 12)
mínimo = salário * 30 / 100
if parcela <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
