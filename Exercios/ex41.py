from datetime import date
nasc = int(input('Qual o ano de nascimento? '))
atual = date.today().year
idade = atual - nasc
if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade <= 20:
    print('Categoria: SENIOR')
else:
    print('Categoria: MASTER')