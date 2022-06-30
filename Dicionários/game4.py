#Crie Um Programa Onde 4 jogadores Joguem Um dado
#e tenham resultados aleatórios.
#guarde esses resultados em um dicionário. no final,
#coloque esse dicionário em ordem, sabend oque o vencedor tirou
#o maior número no dado. 
from random import randint 
from time import sleep
from operator import itemgetter
ranking = {}
dados = {   'Jogador1':randint(1,6),
            'Jogador2':randint(1,6), 
            'Jogador3':randint(1,6),
            'Jogador4':randint(1,6)   }

print('Valores Sorteador:')
for p, i in dados.items():
    print(f'{p:>10} Tirou {i}')
    sleep(0.6)
print('Ranking dos Jogadores:')
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
for c, j in enumerate(ranking):
    print(f'{c+1:>3}º Lugar: Vai para o {j[0]} com {j[1]}')
    sleep(0.6)
