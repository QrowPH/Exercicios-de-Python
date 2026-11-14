dados = list()
pessoas = list()
maior = menor = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    if len(dados) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    dados.append(pessoas[:])
    pessoas.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print(f'Ao todo, você cadastrou {len(dados)} pessoas.')
print(f'O maior peso foi de {maior}. Peso de ', end='')
for p in dados:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {menor}. Peso de ', end='')
for p in dados:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
print()