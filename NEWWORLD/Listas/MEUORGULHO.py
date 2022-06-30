#Faça um progerama que ajude um jogador da MEGASENA.
#O programa vai perguntar quantos jogos serão gerados. 
# e vai sortear 6 Números entre 1 a 60 cada jogo.
#cadstrrando tudo em uma lista composta. 
from random import randint
from time import sleep
mega = []
sena = []
print('=-='*13)
print(f'{"Mega sena":^42}')
print('=-='*13)
a = int(input('Quantos Jogos Deseja: '))
while True:
    while len(mega) != 6:
        r = randint(1,61)
        if r not in mega:
            mega.append(r)
    sena.append(mega[:]) #ele pega as informações que estão sendo jgadas em mega, e manda para sena
    #como se fosse uma cópia, ai fica [[], []] quantos precisar. 
    mega.clear()   #criando uma lista dentro da outra e apos isso ele limpa.
    if len(sena) == a:
            break
print(sena)
for i, k in enumerate(sena):
        print(f'jogo {i+1}: {sorted(k)}')
        sleep(0.6)
print('=-='*13)
print(f'{"Boa Sorte":^42}')
print('=-='*13)