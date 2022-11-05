#faca um programa que receba qualquer text como parametro e mostre uma msenagem com tamanho adaptavel
def seguidor(e):
    s = 0
    for letra in e:
        s = s + 1
    print('=' * s)  
    print(e)
    print('=' * s)


e = str(input('Escreva: '))
seguidor(e)