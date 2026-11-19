def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade}ano : Não vota!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade}ano : VOTO OPCIONAL!'
    else:
        return f'Com {idade} ano : VOTO OPCIONAL!'


print(voto(2000))