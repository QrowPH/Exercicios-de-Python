n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
if média <= 5.0:
    print('Você foi REPROVADO! SEU ANIMAL!')
elif média >= 5.1 and média <= 6.9:
    print('Você está na MÉDIA! SEU BETINHA!')
else:
    print('Você está ACIMA DA MÉDIA! Parabêns farmou aura+ego!')
