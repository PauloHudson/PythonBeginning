 #3 Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar:
produto = int(input('Qual o Preço da Mercadoria? '))
discount = int(input('Qual o percentual(%) de Desconto? '))
preco = int((produto * discount) / 100) 
d = int(produto - preco)
print (f'O Valor a Ser Pago Sera de {d} R$, Com um Desconto de {preco} R$ ({discount}%) Para Um Produto Que Custava {produto} R$')