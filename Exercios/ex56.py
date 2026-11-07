s = media = hvelho = mnova = 0
nomevelho = ''
for c in range(1, 5):
    nome =  str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    s += idade
    if sexo == 'M':
        if idade > hvelho:
            nomevelho = nome
            hvelho = idade
    if sexo == 'F':
        if idade < 20:
            mnova += 1
media = s / 4
print(f'A média de idade é de {media}')
print(f'O nome do homem mais velho tem {hvelho} é se chama {nomevelho}')
print(f'Tem {mnova} mulheres com menos de 20 anos')
