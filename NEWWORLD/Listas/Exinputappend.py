lista = []
#for i in range(0, 3):
#    a = int(input('Digite um valor: '))
#    lista.append(a)
#print(lista)
for i in range(0, 3):
    lista.append(int(input('Digite um Valor: ')))
for c, v in enumerate(lista):
    print(f'Na posição {c} Encontrei o Número {v}!')
  