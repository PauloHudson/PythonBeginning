#Faça Um Programa que leia a o nome e a média
#de um alunio
#guardando também a situação em um dicionário
#no FInla mostre o Conteúdo da estrutura final 
#se ele foi aprovado ou reprovado.
aluno = {} 
aluno['nome'] = str(input('Digite o Seu Nome: '))
media = int(input(f'Média de {aluno["nome"]}: '))
print(f'a Média é igual a {media}')
if media >= 7:
    print('A situação é aprovado')
else: 
    print('Reprovado')
