#crie um programa que leia o nome. ano de nascimento
#carteira de trablho e cadastre os com idade
#em um dicionário, se por acaso o cpts for diferente dezero,
#o dicionario receberá também o ano de contratação
#e o salário. Calcule e acrescente alem da idade, com quantos anos
#vai se aposentar.
#somar(ano de contratção+35)
#subtraria(anodedecotnraração pela data de nascimento)
dados = {}
dados['nome'] = str(input('Digite seu Nome: '))
dados['ano'] = int(input('Ano De Nascimento: '))
dados['carteira'] = int(input('Carteira de Trabalho, Se for = 0 [Cancela]: '))
#if dados['carteira'] == 0:    
dados['contratracao'] = int(input('Ano de Contratação: '))
dados['salario'] = int(input('Digite Seu Salário, R$: '))
dados['periodo'] = 35
dados['contratacao'] + dados['periodo']

#b = a - dados['ano']
#dados['aposentadoria'] = b
#print(dados)