#Crie um Program que leia nome sexo e idade de várias pessoas
#guardando os dadso de cada pessoa em um dicionario e todos os dicionários em uma lista.
#a)Quantas pessoas foram cadastradas
#B)A média de idade do Grupo . #somar os valores e dividir pelo len 
#C)Uma Lista de Todas As Mulheres
#D)Uma lista com todas as Pessoas com idade a cima da Média.
dados = {}
lista = []
listaMédia = []
listaM = []
soma = 0
while True:
    dados['nome'] = str(input('Digite Seu Nome: '))
    dados['idade'] = int(input('Digite Sua Idade: '))
    dados['sexo'] = str(input('Digite o Seu Sexo (M or F): ')).upper()
    lista.append(dados.copy())
    if dados['sexo'] == 'F':
        listaM.append(dados.copy())
    soma = soma + dados['idade']
    continuar = input('Deseja Continuar [S or N]: ').upper()
    if continuar not in 'SN':
        print('DIgite Somente S or N')
    if continuar == 'N':
        print('Obrigado')
        break
print(dados)
print('=-=' * 15)
media = soma / len(lista)
if dados['idade'] >= media:
    listaMédia.append(dados.copy())
print(lista)
print(f'Foram cadastradas um total de {len(lista)} Pessoas.')
print(f'A média de idade é de {media:.1f} Anos')
print('=-=' * 15)
print(f'{"MULHERES CADASTRADAS":>30}')
print('=-=' * 15)
for c, m in enumerate(listaM):
    print(f'A {c+1}ª Mulher se chama {m["nome"]}, Sua Idade é {m["idade"]} Anos')
print('=-=' * 15)
print(f'{"PESSOAS COM IDADE SUPERIOR A MÉDIA":>30}')
print('=-=' * 15)
for x, i in enumerate(listaMédia):
    print(f'=> {i["nome"]} com {i["idade"]} Anos')
