km = float(input('Quantos Km você percorreu? '))
dias = int(input('Quantos dias você quer alugar o carro? '))
total = (dias * 60) + (km * 0.15)
print(f'O total a pagar é de R${total:.2f}')