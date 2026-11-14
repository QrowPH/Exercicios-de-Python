numeros = [[], []]
for c in range(0, 6):
    n = int(input(f'Digite o {c+1} número: '))
    if n % 2 == 0:
        numeros[0].append(n)
    if n % 2 == 1:
        numeros[1].append(n)
print(f'Os número pares são {numeros[0]}')
print(f'Os números impares {numeros[1]}')