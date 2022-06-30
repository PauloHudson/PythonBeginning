#crie uma tupla preenchida com os 20 primeiros colocados da tabela
#do campeonato brasileiro de futebol.
#depois mostre
#a) apenas os 5 primeiros colocados.
#b) os ultimos 4 colocados da tabela
#c) uma lista com os times em rodem alfabética
#d) em qua posição na tabela está o time da chapecoense. 
tabela = ('Corinthians', 'São-Paulo', 'Santos', 'Palmeiras', 'Atlético-Mineiro', 'Real Madrid', 'Barcelona', 'Juventus', 'Chapecoense', 'Birutinhas', 'Alola', 'LosAngeles', 'Gartic', 'CursoEmVídeo', 'Csgo', 'Computador', 'JogadorCaro', 'Bruna', 'Paulo', 'Pokémon')
print('=-='*15)
print(f' Os 5 Primeiros Colocados São: {tabela[0:5]}') 
print('=-='*15)
print(f' Os Quatro Últimos Colocados São: {tabela[-4:]}')
print('=-='*15)
print(f'A Ordem Alfábetica é igual á : {sorted(tabela)} ')
print('=-='*15)
print(f'O time da Chapecoense está na {tabela.index("Chapecoense")+1}ª Posição') #precisei colocar aspas duplas, pois estava dando erro 
#com as aspas simples do começo, o +1 é por conta que começa a contar no 0.
