#faca um programa que leia 5 valorse numericos e guarde em uma lista
#no final mostre qual foi o maior e o menor valor digitado
#e as suas respectivas posições na lista
lista = []
print('=-='* 20)
a = ('Lista Enumerada')
print(f'{a:>35}')
print('=-='* 20)
for i in range(0,5):
    lista.append(int(input('Digite Um Número: ')))
minimo = min(lista)
maximo = max(lista)
print(f'A Lista ficou {lista}')
print(f'Menor Valor foi {minimo} na posição {lista.index(minimo)}')
print(f'maior Valor foi {maximo} na posição {lista.index(maximo)}')