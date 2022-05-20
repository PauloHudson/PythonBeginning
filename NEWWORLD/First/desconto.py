#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

a = int(input('Digite um Valor para receber o desconto: '))
b = a * 0.05
c = a - b
print('O valor do desconto foi de {} e o valor final do produto é {}'.format(b, c))
