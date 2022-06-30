#Crie um Programa que simule o funcionamento de um CAIXAELETRÔNICO
#Deve ser possível ser apenas sacado notas de R$ 50, 20, 10, e 1:
#Programa deve parar quando o valor das notas for = 0
caixa = "Caixa Elêtronico"
print('-' * 50)
print(caixa.center(50))
print('-' * 50)
n = int(input('Digite a Quantia a ser Sacada em R$:'))
while True:
    inteiro_50 = int(n/50)
    resto_50 = int(n % 50) 
    inteiro_20 = int(resto_50 / 20)
    resto_20 = int(resto_50 % 20)
    inteiro_10 = int(resto_20 / 10) 
    resto_10 = int(resto_20 % 10)
    inteiro_1 = int(resto_10)
    if inteiro_50 > 0:
        print(f'Foram Sacadas {inteiro_50} Notas de R$50')
    if inteiro_20 > 0:
        print(f'Foram Sacadas {inteiro_20} Notas de R$20')
    if inteiro_10 > 0:
        print(f'Foram Sacadas {inteiro_10} Notas de R$10')
    if inteiro_1 > 0:
        print(f'Foram Sacadas {inteiro_1} Notas de R$1')
    break
                   