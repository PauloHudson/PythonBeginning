galera = list()
dado = list()
totmaior = 0
totmenor = 0
for info in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for cadapessoa in galera: #vai "ler" dentro da lista, setando como "pessoa" todos dentro de galera, 
    #leitura: para cada pessoa dentro de galera(lista), verifica se é maior ou igual a 21, se for, ele printa o nome (0). "é maior de idade." e soma + 1
    if cadapessoa[1] >= 21: #porque aqui está salvando a idadie, já que dentro da lista, ficou salvo (nome, idade) ai no caso idade serai (1)
        print(f'{cadapessoa[0]} é Maior de idade')
        totmaior += 1
    else:
        print(f'{cadapessoa[0]} é Menor de Idade')
        totmenor += 1

print(f'Temos {totmaior} Maiores e {totmenor} Menores de Idade')