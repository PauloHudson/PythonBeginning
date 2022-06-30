#crie Um Prgorama Onde o Usuário Possa Digitar Vários Valores
#Númericos e Cadastre-os em uma Lista
#Caso O número jà exista Lá Dentro, Ele Não sera Adicionado.
#No finao, Serão Exibidos TOdos os Valores Únicos Digitados. em Ordem Crescente
lista = []
print('=-='*30)
a= ('ORDEMCRESCENTE')
print(f'{a:>50}')
print('=-='*30)
while True:
    digitar = int(input('Digite Um Número: '))
    if digitar not in lista:
        lista.append(digitar)
        Continuar = input('Deseja Continuar [S, N]:').upper()
    else:
        print('Valor Duplicado (DIGITE UM OUTRO VALOR)')
        Continuar = input('Deseja Continuar [S, N]:').upper()
    if Continuar == 'N':
        lista.sort()
        print('=-='*30)
        print(f'A Ordem Crescentes dos Números É {lista}')
        print('=-='*30)
        break