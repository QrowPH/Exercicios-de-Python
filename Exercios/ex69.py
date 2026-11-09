maior18 = homem = mulher = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    if resp == 'N':
        break
print(f'A) Tem {maior18} pessoas maiores de 18 anos')
print(f'B) Tem {homem} homens cadastrados')
print(f'C) Tem {mulher} mulheres com menos de 20 anos')
