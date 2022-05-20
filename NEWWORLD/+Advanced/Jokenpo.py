from random import random


import random
print('Jokenpo Onlike By Paulo')
print('-' * 50)
jokenpo = input('Pedra, Papel ou Tesoura? ')
lista = ['Pedra', 'Papel', 'Tesoura']
escolhido = random.choice(lista)
if jokenpo == 'Pedra' and escolhido == 'Papel':
    print('Papel Maior que Pedra, Perdeu!!')
elif jokenpo == 'Pedra' and escolhido == 'Tesoura':
    print('Pedra Maior que tesoura, Parabéns!')
elif jokenpo == 'Pedra' and escolhido == 'Pedra':
    print('Pedra igual a Pedra, Jogue Novamente!')
elif jokenpo == 'Papel' and escolhido == 'Papel':
    print('Papel igual a Papel, Jogue Novamente!')
elif jokenpo == 'Papel' and escolhido == 'Tesoura':
    print('Tesoura maior que Papel, Perdeu!')
elif jokenpo == 'Papel' and escolhido == 'Pedra':
    print('Papel Maior que Pedra, Parabéns!') 
elif jokenpo == 'Tesoura' and escolhido == 'Tesoura':
    print('Tesoura igual a Tesoura, Jogue Novamente!')
elif jokenpo == 'Tesoura' and escolhido == 'Pedra':
    print('Pedra maior que Tesoura, Perdeu')
elif jokenpo == 'Tesoura' and escolhido == 'Papel':
    print('Tesoura maior que Papel, Parabéns!')
print('-' * 50)
print('FIM')

