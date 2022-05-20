print('Compras no Varejo.Com')
print('-' * 40)
valor = float(input('Olá, Digite o Valor do Produto!: '))
print('(a vista, cartão, 2x cartão, 3x cartão.)')
condicao = input('Como Deseja pagar? (Digite uma das condições acima): ')
if condicao == 'a vista' or condicao == 'A vista':
    x = valor - (valor * 0.1) 
    print(f'O valor a ser pago com 10% de desconto será de {x}R$')
elif condicao == 'cartão' or condicao == 'Cartão' or condicao == 'cartao':
    x1 = valor - (valor * 0.05) 
    print(f'O valor a ser pago com 5% de desconto será de {x1}R$')
elif condicao == '2x Cartão' or condicao == '2x cartao':
    print(f'Valor a ser pago sem desconto!! Total de {valor}R$')
elif condicao == '3x cartão' or condicao == '3x cartao':
    x2 = valor + (valor * 0.2) 
    print(f'O valor a ser pago com 20% de juros desconto será de {x2}R$')
print('-' * 40)

