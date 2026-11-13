números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado, por gente')
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print('-=' * 30)
print(f'Você digitou os valores {números}')