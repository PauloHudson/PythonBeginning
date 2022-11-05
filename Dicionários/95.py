#Aprimore o Desafio 93 Para que ele funcione com varios Jogadores.
#incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
#Crie um Programa que gerencie o AProveitamento de um jogador de futebol.
#o programa vai ler o nome do jogador e quantas partida sele jogou.
#depois de ler a quantidade de gols feitos em cada partida. 
#no final tudo sera guardado em um dicionário incluindo o toal de gols feitos durante o campeonato.
dados = {}
jogos = []
geral = []
while True:
    dados['Nome'] = input('Nome do Jogador.: ')
    partidas = int(input(f'Quantas Partidas o {dados["Nome"]} Jogou? '))
    for c in range(partidas):
        jogos.append(int(input(f'Quantos Gols Na {c+1} Partida: ')))
    dados['Gols'] = jogos[:]
    jogos.clear()
    dados['Total'] = sum(jogos)
    geral.append(dados.copy())
    continuar = input('Dejesa Continuar [S or N]: ').upper()
    if continuar not in 'SN':
        print('Digite Somente SIM OU NÃO (S or N)')
    if continuar == 'N':
        break
print('=-=' * 15)
print(f'{"Cod"} {"Nome":>3} {"Gols":>10} {"Total":>25}')
print('-'*45)
for c, i in enumerate(geral):
    print(f'{c}  {i["Nome"]:<7}     {i["Gols"]!s:<12s}             {i["Total"]:5>}')
print('-'*45)
while True:
    levantamento = int(input('Mostar Os dados de Qual Jogador? (999 Para).: '))
    if levantamento == 999:
        print('Thanks')
        break

    if levantamento >= len(geral):
        print(f'Digite Somente Entre 0 e {len(geral)}')

    else:
        print(f'{"=>":>3} Levantamento Do Jogador {geral[levantamento]["Nome"]}:')
        for b, f in enumerate(geral[levantamento]['Gols']):
            print(f'{"=>":>3} No Jogo {b+1} Fez {f} Gols.')
    print('='*45)