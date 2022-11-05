def area(a, b): #está recebendo a e b
    m = a * b
    print(f'A área de um Terreno de {a}x{b} é de {m}m²')


print(' Controle de Terrenos')
print('=-=' * 15)
a = int(input('Largura (m): '))
b = int(input('Comprimento (m): '))
area(a, b)



