velocidade = float(input('Qual é a velocidade do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Multado! Você execeu o limite de velocidade')
    print(f'Você deve pagar uma multa de R${multa:.2f}')
print('Tenha um bom dia! Dirija com segurança!')