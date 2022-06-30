#crie um programa que crie uma matriz de dimensoes 3x3 e prencha os valores lidos pelo teclado. 
matriz = [[], [], []] #0,0,0
for l in range (0, 3): #para cada linha, havera quatro colunas
   for c in range(0,4): #para cada coluna
        matriz[l].append(int(input(f"Digite um valor para [{l},{c}]: ")))
print('-='*30)
for l in range(0,3): #mesma coisa, para cada linha, havera qutro colunas. 
    for c in range(0,4):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()