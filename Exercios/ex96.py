def area(larg, comp):
    area = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {area}')


l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l,c)