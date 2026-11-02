from math import radians, sin, cos, tan
num = int(input('Diga um ângulo: '))
seno = sin(radians(num))
print(f'O ângulo de {num} tem o seno de {seno:.2f}')
cosseno = cos(radians(num))
print(f'O ângulo de {num} tem o cosseno de {cosseno:.2f}')
tangente = tan(radians(num))
print(f'O ângulo de {num} tem o tangente de {tangente:.2f}')