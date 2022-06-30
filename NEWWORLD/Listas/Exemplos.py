lista = [1, 2, 3, 4, 5, 6]
lista.append(5) #adicionará o valor 5 ao último valor, no caso 6
lista.insert(1, 66) # vai adicionar 66, no lugar do 1 valor, caso 2, fazendo ele ir para a esquerda
# e 66 ocupando o espaço dele
if 2 in lista: # vai verificar se há o número 2 na lista
    print('Há 2 na lista')
lista.sort() # vai ordenar a lista
#print(lista.sort(reverse=True)) # vai printar a lista ordenada ao contrario 
print(f'há {len(lista)} valores dentro desta lista') # vai contar
#quantos valorees há dentro da lista
#lista.pop() #vai remover o último valor no caso 1
lista.pop(5) #atribuimos valor de remoção removera o 6
lista.remove(66) #remove não pela posição, mas sim pelo conteudo
print(lista)
for _ in range (5):
    print('amor') 
del(lista(2))