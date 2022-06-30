#Crie um Programa onde o usuario possa digitar cinco valores
#e cadastre os em uma lista
#ja na posição correta de inserção sem usar o sort
#no final mostre a lsita ordenada 
numeros = []
for _ in range(5):
    numero = int(input("Digite um número: "))
    for chave, valor in enumerate(numeros):
        if numero < valor:
            numeros.insert(chave, numero)
            break
    else:
        numeros.append(numero)
    print("Lista atual:", numeros)