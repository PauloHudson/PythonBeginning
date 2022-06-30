#Crie um Programa que vai ler varios núemros em uma lista
#depois diosso mostre
#A) Quantos Números foram digitados
#B) A lista de Valores Ordenados De foram decrescente
#C) Se o Valor 5 Foi Digitado e está ou não Na lista
lista = []
cont = 0
while True: 
    digitar = lista.append(int(input('Digte um Valor: ')))
    continuar = input('Deseja Continuar [S, N]:').upper()
    cont = cont + 1
    if continuar == 'N':
        print('=-='* 20)
        lista.sort(reverse=True)
        if 5 in lista:
            print('O Valor 5 Está Presente na Lista')
        else:
            print('O Valor 5 Não está presente na Lista!')    
        print(lista)
        break