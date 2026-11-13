palavras = ('Elsword','Aisha', 'Rena', 'Raven', 'Eve', 'Chung', 'Ara', 'Elesis',
            'Add', 'LuCiel', 'Rose', 'Ain', 'Laby', 'Noah', 'Lithia')
for p in palavras:
    print(f'\nNo Nome {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')