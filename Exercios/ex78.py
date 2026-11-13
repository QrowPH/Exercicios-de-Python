números = []
maior = menor = 0
for c in range(0, 5):
    números.append(int(input(f'Digite um valor para a posição {c+1}: ')))
    if c == 0:
        maior = menor = números[c]
    else:
        if números[c] > maior:
            maior = números[c]
        if números[c] < menor:
            menor = números[c]
print('-=' * 30)
print(f'Você digitou os valores {números}')
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')