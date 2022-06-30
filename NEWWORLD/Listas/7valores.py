from random import randint
from time import sleep
mega = list()
sena = list()
print('-'*40)
print('JOGA NA MEGA SENA'.center(40))
print('-'*40)
sort = int(input('Quantos jogos voce quer que eu sorteie? '))
while True:
    while len(mega) != 6:
        x = randint(0, 60)
        if x not in mega:
            mega.append(x)
    sena.append(mega[:])
    mega.clear()
    if len(sena) == sort:
        break
for l, j in enumerate(sena):
    print(f'Jogo {l+1}: {sorted(j)}')
    sleep(0.5)