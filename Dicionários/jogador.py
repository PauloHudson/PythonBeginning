#Crie um Programa que gerencie o AProveitamento de um jogador de futebol.
#o programa vai ler o nome do jogador e quantas partida sele jogou.
#depois de ler a quantidade de gols feitos em cada partida. 
#no final tudo sera guardado em um dicionário incluindo o toal de gols feitos durante o campeonato.
dados = {}
jogos = []
while True:
    dados['Nome'] = input('Nome do Jogador.: ')
    partidas = int(input(f'Quantas Partidas o {dados["Nome"]} Jogou? '))
    for c in range(partidas):
        jogos.append(int(input(f'Quantos Gols Na Partida {c+1}: ')))
        dados['Gols'] = jogos[:]
        dados['Total'] = sum(jogos)
    break
print('=-=' * 15)
print(dados)
print('=-=' * 15)
print(f'O jogador {dados["Nome"]}')
print(f'Marcou um total de {dados["Total"]} Gols')
print(f'Marcando {dados["Gols"]}')
print('=-=' * 15)
print(f'O jogador {dados["Nome"]}, Jogou {partidas} Partidas.')
for p, i in enumerate(jogos):
    print(f'{"=>":>5} Na Partida {p+1}, Fez {i} Gols. ')
print(f'{"=>":>5} Total de {dados["Total"]} Gols'.upper())