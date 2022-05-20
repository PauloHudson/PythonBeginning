print('Bem vindo ao BRUPH processor!')
print('*'*40)
valor1 = int(input('Digite o Valor a ser Processado: '))
valor2 = int(input('Digite o Segundo Valor a ser Processado: '))
print('*'*40)
opcao = 0
print('[1] Soma')
print('[2] Substração')
print('[3] Divisão')
print('[4] Multiplicação')
print('[5] Digitar Novamente')
print('[6] Sair')
escolhas = [1, 2, 3, 4, 5, 6]
erro =('Digite somente uma das opçoes')
print('*'*40)
while opcao != escolhas:
    opcao = int(input('Digite uma Opção: '))      
    if opcao == 1:
        print('Você selecionou [Adição]')
        print(f'O seu resultado foi {valor1 + valor2} ')
    elif opcao == 2:
        print('Você selecionou [Subtração]')
        print(f'O seu resultado foi {valor1 - valor2} ')
    elif opcao == 3:
        print('Você selecionou [Divisão]')
        print(f'O seu resultado foi {(valor1 / valor2):.2}')
    elif opcao == 4:
        print('Você selecionou [Multiplicação]')
        print(f'O seu resultado foi {valor1 * valor2} ')
    elif opcao == 5:
        valor1 = int(input('Digite o Valor a ser Processado: '))
        valor2 = int(input('Digite o Segundo Valor a ser Processado: '))
    elif opcao == 6:
        print('Fim')
        quit()
    else:
        print(erro)