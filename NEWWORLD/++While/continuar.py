#validador de numero3
#digitar vários valores e o programa vai pedir para parar
#quando parar vai ser digitado o menor e maior valor
array = []
comecar = str(input('Começar -- [S or N]: ')).upper()
if comecar == 'N':
    print('Volte Novamente')
while comecar == 'S':
    valor = int(input('Digite um valor.: '))
    comecar = str(input('Você Deseja Continuar?: ')).upper()
    array.append(valor)
    if comecar != 'S':
        print(f'Os Valores Foram {array}')
        mino = min(array)
        print(f' O Menor valor Encontrado foi de {mino}')
        maxi = max(array)
        print(f' O Maior valor Encontrado foi de {maxi}')