from asyncio.proactor_events import _ProactorDuplexPipeTransport
from random import randint
i = 0
palpite = randint(1, 10)
#print(palpite)
print('-'*70)
print('OLÁ BEM VINDO AO BRUGAMES.5000')
print('VOCÊ TENTARÁ ACERTAR O VALOR ESCOLHIDO PELO COMPUTADOR ENTRE [1, 10]')
print('-'*70)
computador = int(input('Digite um número: '))
while palpite != computador:
    computador = int(input('Digite um número Novamente: '))
    i = i + 1 
print('-'*70)
print(f'Parabéns, Você acertou com {i} tentativa(s)') 

  
   

