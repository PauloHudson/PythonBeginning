#a1 = int(input('Digite o Primeiro Valor:'))
#a2 = int(input('Digite o Segundo Valor:'))
#a3 = int(input('Digite o Terceiro Valor:'))
#maximo = max(a1, a2, a3)
#minimo = min(a1, a2, a3)
#print(f'o maior valor é {maximo}')
#print(f'o menor valor é {minimo}')
lista = []
for i in range(0,3):
    lista.append(int(input('Digite um valor: ')))
mini = min(lista)
maxi = max(lista)
print(f'O Maior Valor foi {maxi}, O menor {mini}')