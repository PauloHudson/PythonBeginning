from random import randint
from numpy import append
#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, 
#e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas')
print('*'*40)
print('Bem vindo a Temperaturas5000.')
print('Digite A quantidade de Temperaturas necessárias fornecidadas Abaixo Para Que Sejá Calculada A:\n(Média e Maior Temperatura no Período.)')
print('*'*40)
i = 0
somax = 0
array = []
pick = randint(1, 5)
count = pick
print(f'Você Precisará Digitar a Temperatura {pick} Vezes ')
print('*'*40)
while i < count:
    temperatura = float(input('Digite a Temperatura: '))
    array.append(temperatura)
    soma = temperatura + somax
    somax = soma
    i = i + 1 
print('*' * 40)
media = float(somax / pick)
print(f'A média é de {media}')
print('*' * 40)
#print(array)
minimo = min(array)
print(f'Temperatura Mínima é {minimo}')
maximo = max(array)
print(f'Temperatura Máxima é {maximo}')
