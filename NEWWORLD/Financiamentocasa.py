print ('-' * 20)
print('Olá Seja Bem Vindo ao Sistema de Empréstimos.')
print('Para Começar Digite as informações a baixo:')
print ('-' * 20)
casa = int(input('Valor da Casa:'))
salario = float(input('Seu Salário:'))
anos = int(input('Quantos anos a pagar:'))
valor_parcelas = int(casa / 12 ) / anos
salariodele = (salario * 0.30)
print ('-' * 20)
if salariodele > valor_parcelas:
    print('Parabéns, Sua renda é compatível com o nosso sistema de crédito, o valor sera liberado em 24hrs!.')
    print(f'Segundo a nossa simulação o valor da fatura será de {valor_parcelas:.5}R$, em {anos} Anos, ou {anos * 12} Meses')
else:  
    print('Infelizmente sua renda não será compatível, mas você pode tentar fazer outra simualação!.')
print('------Fim------')
