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
i = 0
array = []
if wish == "S" or wish == 's':
     print('*'*40)
     print('Especificação   Código  Preço')
     print('Cachorro Quente 100     R$ 1,20')
     print('Bauru Simples   101     R$ 1,30')
     print('Bauru com ovo   102     R$ 1,50')
     print('Hambúrguer      103     R$ 1,20')
     print('Cheeseburguer   104     R$ 1,30')
     print('Refrigerante    105     R$ 1,00')
     print('*'*40)
     escolhas = [100, 101, 102, 103, 105]
     while i != escolhas:
          cardapio = int(input('Digite Agora as Opções Desejadas (uma a um)!: '))
          array.append(cardapio)
          a3 = str(input('Deseja Parar? [S, N]: ')).upper 
          if a3 == 'n' or a3 == 'N':
               cardapio = int(input('Digite Agora as Opções Desejadas (uma a um)!: '))
               i = i + 1
          elif a3 == 's' or a3 == 'S':
               print('total a pagar')
          
else:
    print('Fique A vontade para Voltar outro dia.')
     
