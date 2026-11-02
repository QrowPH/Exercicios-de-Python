altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = altura * largura
tinta = area / 2
print(f'A parede tem {altura}x{largura} e a área dela é de {area} e o consumo de tinta para pintar'
      f'será de {tinta:.2f}')