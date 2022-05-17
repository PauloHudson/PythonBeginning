#2 - Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário 
# e a porcentagem do aumento. Exiba o valor do aumento e do novo salário:
salario = int(input('Qual o seu Salario: '))
aumento = int(input('Quantos % de Aumento vc Teve? '))
c = int((salario * aumento) / 100) + salario
ganhoreal = (c - salario)
print(f'Voce teve um aumento de {aumento}% e seu novo salario salario agora é {c}R$ (Representando um aumento real de {ganhoreal}R$ em comparacao aos {salario}R$ que vc recebia).') 