#validador de numero3
#digitar vários valores e o programa vai pedir para parar
#quando parar vai ser digitado o menor e maior valor
i = 0
comecar = str(input('Começar -- [S or N]: ')).upper()
print('Volte Novamente')
array = []
while comecar < i:
    if comecar == 'S':
        valor = int(input('Digite um valor.: '))
        comecar = str(input('Você Deseja Continuar?: ')).upper()
        array.append(valor)
    if comecar != 'S':
        break
mino = min(valor)
print(mino)