#Qual o Total Gasto?
#Quatos Produtos Custam maisde 1000 R$
#qual o nome do produto mais barato
print('-' * 40)
print('LOJA DO PAULÃO')
print('-' * 40) 
total = 0 #Total da Compra
barato = 0 # Nome do Produto Mais Barato
contadormil = 0 #Soma quantos produtos a cima de 1000
produtopreco = {} #Define Lista
while True:
    produto = input('Nome Do Produto: ').upper()
    preco = int(input('Digite O Valor do Produto: '))
    total = total + preco
    if preco > 1000:
        contadormil = contadormil + 1
    produtopreco[produto] = preco
    #calcular
    minimo = min(produtopreco.values()) #pega o menor valor
    minproduto = min(produtopreco, key=produtopreco.get) #pega o nome do menor valor. 
    stop = input('Deseja Continuar [S ou N]: ').upper()
    if stop == 'S':
        produto = input('Nome Do Produto: ').upper()
        preco = int(input('Digite O Valor do Produto: '))
        if preco > 1000:
            contadormil = contadormil + 1
        stop = input('Deseja Continuar [S ou N]: ').upper()
        total = total + preco
    if stop == 'N':
        print('-' * 40)
        print(f'A compra foi um total de R${total:.2f} ')
        print(f'Temos {contadormil} Produto(s) a cima de R$1000')
        print(f'O produto mais barato foi {minproduto} custando R${minimo:.2f}')
        print('-' * 40)
        break
        