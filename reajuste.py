#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
a = int(input('Digite o valro do seu salário: '))
b = a * 0.15
c = b + a 
print('o valor do reajude foi de {} ou 15% do seu salário, e agora seu salário é {}.'.format(b, c))