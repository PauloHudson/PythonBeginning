pessoa = {'Nomes': 'Paulo', 'Sexo': 'M', 'Idade': 22 }
pessoa['Peso'] = 98.5
#print(pessoa['Idade'])
#print(f'o {pessoa["Nomes"]} tem {pessoa["Idade"]} Anos')
#print(pessoa.keys()) #Printa os índices Nomes, Sexo, Idade.
#print(pessoa.items()) #Printa tudo.
#print(pessoa.values()) #são os itens do dic. = Paulo,M,22
for k, v in pessoa.items(): #k e v são variáveis aleatórias que
    print(f'{k} = {v}') #se tornam(keys e values) indices e itens

for d in pessoa.values(): #Printara os valores
    print(d)
for g in pessoa.keys(): #Printara os ìndices
    print(g)

#Adicionar
