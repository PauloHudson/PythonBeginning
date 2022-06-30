from calendar import c
from this import d

#gerar 5 valores aleatórios, e o programa dira o maior e o menor.
from random import randint
a = randint(0, 20)
b = randint(0, 20)
c = randint(0, 20)
d = randint(0, 20)
e = randint(0, 20)
tupla = (a, b, c, d, e)
maxi = max(tupla)
mini = min(tupla)
print(tupla)
print(f'O Maior Valor foi {maxi}, O Menor {mini}')