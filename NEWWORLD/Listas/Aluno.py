#Crie um Programa que leia o nome e duas Notas
#guarde tudo em uma lista composta.
#No Final, Mostre um boletim Contendo a Média
#De cada um e permita que o usuario possa mostras as notas de cada aluno.
boletim = []
while True:
    nome = str(input('Digite Seu Nome: '))
    nota_1 = float(input('Nota1: '))
    nota_2 = float(input('Nota1: '))
    escolha = input('Deseja Continuar? [S or N]').upper()
    media = (nota_1 + nota_2) / 2
    boletim.append([nome, [nota_1, nota_2], media])
    if escolha not in 'SN':
        print('Digite somente S or N')
    if escolha == 'N':
        break

print(f'{"NOME":<14}{"Notas":<19}{"Média":<21}')
print('-'* 43)
for i, b in enumerate(boletim):
    #print(f'{i+1:<2} nome{b[0]} notas{b[1][0]} notas{b[1][1]} media{b[2]}')
    print(f'{i:<2}{b[0].upper():<11} {b[1][0]},  {b[1][1]} {b[2]:>14}')
print('-'* 43)
while True:
    a = int(input('Deseja Mostrar A nota de Qual Aluno [999 intrrompe]?'))
    print(f'as notas de {boletim[a][0]} São: {boletim[a][1][0]}, {boletim[a][1][1]}')
    if a == 999:
        break