#exercício com o professor
#FACA UM PRORGRAMA QUE LEIA O NOME E PESO DE VÁRIAS PESSOAS. 
#GUARDANDO TUDO EM UMA LISTA. 
#NO FINAL MOSTRE
#QUANTAS PESSOAS FORAM CADASTRADAS. 
#UMA LISTAGEM COM AS PESSOAS MAIS PESADAS.
#UMA LISTAGEM COM AS PESSOAS MAIS LEVES.
temp = []
principal = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: '))) #jogando informações em temp
    temp.append(float(input('Peso: '))) #jogando informações em temp
    if len(principal) == 0: #se eu não cadastrei ninguem ainda em principal, se o tamanho for igual a 0
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    principal.append(temp[:]) #Criando uma Cópia do Temp e jogando em principal
    temp.clear() #limpando informações de Temp
    resposta = str(input('Quer continuar [S or N]'))
    if resposta not in 'SsNn': #se a reposta não foir igual a S de sim ou N de não, ele printa
        print('Digite Somente S ou N')
    if resposta in 'Nn': #se a reposta for igual a Nn ele da break e executa o print debaixo
        break

print('=-=' * 15)
print(f'Foram Cadastradas um total de {len(principal)} Pessoas') #len pega o total de informações dentro de uma lista, aí não precisaria usar o contador (cont)
print(f'A lista é Igual á {principal}')
print(f'O Maior peso foi de {maior}Kg., Peso de ', end='')
for p in principal:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print()
print(f'O Menor Pesoa foi de {menor}Kg., peso de ', end='')
for p in principal:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
print()