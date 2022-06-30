#Escreva um programa que leia um número
#E escreva ele por extenso, de 0 a 20
#Se for um valor diferente de 0 a 20, De erro.
tupla = ('Zero','Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
a = int(input('Digite um Número de 0 a 20: '))
if a >20 or a < 0:
    print('Digite novamente, Número Inválido')
    a = int(input('Digite Somente um Número de 0 a 20: '))
print(f'Você Digitou o Número {tupla[a]}')