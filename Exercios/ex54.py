from datetime import date
atual = date.today().year
maior = menor = 0
for c in range(1, 8):
    nasc = int(input('Em que ano você nasceu? '))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Tem {maior} pessoas maiores de idade')
print(f'Tem {menor} pessoas menores de idade')