#desenvolva um programa que leia quatro valores pelo teclado.
#e os guarde em uma tupla
# no finla mostre:
#a) Quantas vezes apareceram o número 9
#b) Em que posição Foi Digitado o Primeiro Valor 3
#c) Quais FOram os Número Pares
a = int(input('Digite Um Valor: '))
b = int(input('Digite Mais Um Valor: '))
c = int(input('Digite Mais um Valor: '))
d = int(input('Digite O Último Valor: '))
tupla = (a, b, c, d)
print(f'Você Digitou {tupla}')
print(f'O Número 9 Apareceu {tupla.count(9)} Vezes')
if 3 in tupla:
    print(f'O Número 3 Apareceu na Posição {tupla.index(3)+1}')
else:
    print('O Número 3 não foi Digitado')
print(f'Os valores pares foram ',end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')