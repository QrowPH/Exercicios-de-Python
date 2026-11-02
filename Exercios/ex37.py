num = int(input('Digite um valor: '))
print('''Conversor de valores:
[ 1 ] Converter para BINARIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opção = int(input('Diga sua opção: '))
if opção == 1:
    print(f'A conversão de {num} para binario é {bin(num)[2:]}')
elif opção == 2:
    print(f'A conversão de {num} para octal é {oct(num)[2:]}')
elif opção == 3:
    print(f'A conversão de {num} para hexadecimal é {hex(num)[2:]}')
