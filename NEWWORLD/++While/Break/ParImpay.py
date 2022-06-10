#COmputador vai escolher um valor
#escolherei outro, nisso escolheremos par ou impar. 
# mostrar a quantidade de Vitórias que consegui.
# jogo só para quando o perder.
# par ou impar entre 0 e 10
from random import randint
print('=-=' * 15)
print('LETS PLAY PAR OU IMPAR?')
print('---' * 15)
computador = randint(0, 15)
contador = 0
while True:
    pessoa = int(input('Digite um Valor: '))
    print('---' * 15)
    parimpar = input('Par ou Ímpar [I, P]:').upper()
    if parimpar == 'P':
        soma = (computador + pessoa)
        if soma % 2 == 0:
            print(f'Você jogou {pessoa} e o Computador {computador}. Total = {computador + pessoa} (PAR)')
            print('---' * 15)
            print('Você Venceu.')
            print('---' * 15)
            print('Vamos Jogar NOVAMENTE...')
            print('---' * 15)
            contador = contador + 1
        else:
            print('---' * 15)
            print(f'Você jogou {pessoa} e o Computador {computador}. Total = {computador + pessoa} (IMPAR)')
            print('=-=' * 15)
            print(f'GAME OVER, Você Venceu {contador} Vezes')
            print('><' * 15)
            break
    if parimpar == 'I':
        soma = (computador + pessoa)
        if soma % 2 == 1:
            print(f'Você jogou {pessoa} e o Computador {computador}. Total = {computador + pessoa} (IMPAR)')
            print('---' * 15)
            print('Você Venceu.')
            print('---' * 15)
            print('Vamos Jogar NOVAMENTE...')
            print('---' * 15)
            contador = contador + 1
        else:
            print('---' * 15)
            print(f'Você jogou {pessoa} e o Computador {computador}. Total = {computador + pessoa} (PAR)')
            print('=-=' * 15)
            print(f'GAME OVER, Você Venceu {contador} Vezes')
            print('><' * 15)
            break