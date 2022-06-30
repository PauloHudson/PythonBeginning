#Crie um Programa que leia Varios Números e coloce que uma lista
#depois disso crie duas listas extras que vao conter apenas
#os valores pares e os valores impares
#ao final mostre o conteudo das tres listas geradas.
print('=-='* 20)
listamestre = []
par = []
impar = []
while True:
    a = int(input('Digite Um Valor: '))
    listamestre.append(a)
    if a % 2 == 0:
        par.append(a)
    else:
        impar.append(a)
    continuar = input('Deseja Parar [S or N]: ').upper()
    if continuar == 'S':
        print('=-='* 20)
        print(f'Lista Completa: {listamestre}')
        print(f'Pares: {par}')
        print(f'Impares: {impar}')
        break

