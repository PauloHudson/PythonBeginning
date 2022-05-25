
print('Sequencia de Fibonacci')
print('Programa consiste em Digiar valor [N] e em sequência lhe mostrará a sequencia Fibonnaci deste número.')
#Fibonnaci exemplo(número anterior + o sucessor.)
#ex: 1, 1, 2, 3, 5, 8, 13...
#F(n + 2) = F(n + 1) + F(n) , com n ≥ 1 e F(1) = F(2) = 1
n = int(input('Quantos Valores serão mostrados: '))
a = 0
b = 1
cont = 3 
print(a)
print(b)
while cont <= n:
    x = a + b
    print(x)
    a = b
    b = x
    cont = cont + 1 
