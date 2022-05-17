##Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
carro = int(input('Quantos KM foram percorridos? '))
dias = int(input('Quantos Dias o carro foi alugado? '))
valor = (dias * 60)
km = (carro * 0.15)
print('O valor a ser pago será de {}, valor por dia de {} e por km de {}'.format(valor+km, valor, km))