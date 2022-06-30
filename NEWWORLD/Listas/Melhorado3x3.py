#crie um programa que crie uma matriz de dimensoes 3x3 e 
# prencha os valores lidos pelo teclado. 
#aprimorar o desafio Anterior
#A) strando A soma de Todos os Valores Pares.
#B) soma dos Valores da terceira Coluna
#C) O maior valor da Segunda Linha. 
matriz = [[], [], []] #cada matriz dessa 0,1,2
par = []
#recebera os valores do input, organizando de três em três 000.000.000
for l in range(0, 3): #Para 3 Linhas, haverão 3 Colunas
    for c in range (0, 3):
        a = int(input(f'Digite os Valores de [{l}][{c}]: '))
        matriz[l].append(a)
        if a % 2 == 0:
            par.append(a)
for l in range(3):
    for c in range(3):
        #print(f'{matriz[linha][coluna]}', end='')
        print(f'[{matriz[l][c]:^5}]', end='') #o ^ faz com que ele de um espaçamento
    print()
maior = max(matriz[1])
print(f'Os valores Pares são Iguais á {sum(par)}')
print(f'A soma dos valores da terceira lista é {sum(matriz[2])}')
print(f'O maior valor da Segunda Lista é {maior}')
