n = int(input('Digite um número: '))
s = c =0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        s += n
        c += 1
print(f'Você digitou {c} valores e a soma entre eles é de {s}')