n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print("""MENU
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR 
    [ 4 ] NOVOS NUMEROS 
    [ 5 ] SAIR """)
    opção = int(input('Qual sua opção: '))
    print('-=' * 20)
    if opção == 1:
        soma = n1 + n2
        print(f'A soma dos valores {n1} + {n2} = {soma} ')
    elif opção == 2:
        multiplicar = n1 * n2
        print(f'A multiplicação dos valores {n1} * {n2} = {multiplicar} ')
    elif opção == 3:
        if n1 > n2:
            maior = n1
            print(f'O maior número entre os valores {n1} e {n2} é {maior}')
        if n1 < n2:
            maior = n2
            print(f'O maior número entre os valores {n1} e {n2} é {maior}')
    elif opção == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
