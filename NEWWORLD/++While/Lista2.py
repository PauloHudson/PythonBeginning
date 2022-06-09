# O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
# Considere que o cliente deve informar quando o pedido deve ser encerrado.

print('Bem Vindo A Nossa Padaria')
print('Desenvolvemos um Programa que lhe Mostrará o Cardápio automáticamente.')
print('Siga os Paços A Seguir!.')
wish = str(input('Você deseja Ver o Cardápio Agora? [S, N]: '))
escolhax = 'S' or 's'
array = []
a = ('Cachorro Quente')
b = ('Bauru Simples')
c = ('Bauro com Ovo')
d = ('Hambúrguer')
e = ('Cheseburguer')
f = ('Regrigerante')
if wish == "S" or wish == 's':
     print('*'*40)
     print('Especificação   Código  Preço')
     print('Cachorro Quente A    R$ 1,20')
     print('Bauru Simples   B    R$ 1,30')
     print('Bauru com ovo   C    R$ 1,50')
     print('Hambúrguer      D    R$ 1,20')
     print('Cheeseburguer   E    R$ 1,30')
     print('Refrigerante    F    R$ 1,00')
     print('*'*40)
     while escolhax == 'S':
        produto = str(input('Qual Produtos você deseja (Digite Somente o Código)? '))
        if produto == a:
            print(f'Você selecionou {quantidade}{a} ')
        quantidade = int(input('Digite Agora a Quantide: '))
        escolhax = str(input('Deseja Acrescentar Algo? [S or N]: ')).upper


