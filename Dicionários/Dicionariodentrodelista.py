#DICIONÁRIO DENTRO DE LISTA
from pandas import read_json


lista = []
estado1 = {'uf':'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'uf':'São Paulo', 'Sigla': 'SP'}
lista.append(estado1)
lista.append(estado2)
print(lista[0]['Sigla']) #= rj
print(lista[1]['uf']) # São Paulo