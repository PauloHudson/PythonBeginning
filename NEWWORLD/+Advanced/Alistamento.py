print('BEM VINDO AO SISTEMA DE ALISTMENTO')
nome = input('digite seu nome:')
data = int(input('digite sua data de nascimento:'))
datax = (2022 - data)
if datax < 18:
    print(f'Olá {nome} ainda não chegou a sua vez de se alistar, mas falta pouco apenas {18 - datax} Ano(s)!')
    print('Esperamos por você')
elif datax == 18:
    print('Parabéns, chegou o tão esperado dia, venha e aliste-se!')
else:
    print('Já passou da hora de se alistar, aliste-se e regularize-se!')
print('-----Fimm-----')