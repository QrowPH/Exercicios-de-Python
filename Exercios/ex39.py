from datetime import date
anonasc = int(input('Em que ano você nasceu? '))
anoatual = date.today().year
idade = anoatual - anonasc
if idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o Alistamento')
elif idade == 18:
    print(f'Você tem {idade} anos. VOCÊ PRECISA SE ALISTAR AGORA!')
elif idade > 18:
    print(f'Você já deveria ter se alistado há {idade - 18} anos')
