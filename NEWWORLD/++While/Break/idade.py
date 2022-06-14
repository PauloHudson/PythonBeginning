#Crie um Programa que leia a Idade e o sexo de varias pessoas.
#A cada Pessoa Cadastrada o Programa Deve Perguntar se a Peossa quer continuar.
#No final mostre:
#A) Quantas Pessoas tem mais de 18 anos.
#B) Quantos Homens foram cadastrados.
#C) Quantas Mulheres tem menos de 20 anos.
print('-=' * 30)
print('Bem Vindo Ao Programa de Cadastro')
print('-=' * 30)
contador18 = 0 #contador de pessoas com mais de 18 anos
contador = 0 #contador de pessoas cadastradas
sexoh = 0 #contador de homens
while True:
    pessoa = int(input('Digite a Idade da Pessoa: '))
    if pessoa >= 18:
        contador18 += 1
    sexo = (input('Digite o Sexo da Pessoa [H ou M]: ')).upper()
    if sexo == 'M':
        if pessoa < 20:
            contador += 1
    if sexo == 'H':
        sexoh += 1
    stop = (input('Deseja Continuar? [S/N]: ')).upper()
    if stop == 'S':
        pessoa = int(input('Digite a Idade da Pessoa: '))
        sexo = (input('Digite o Sexo da Pessoa [H ou M]: ')).upper()
        if pessoa >= 18:
            contador18 += 1
        if sexo == 'M':
            if pessoa < 20:
                contador += 1
        if sexo == 'H':
            sexoh += 1
        stop = (input('Deseja Continuar? [S/N]: ')).upper()
    if stop == 'N':
        print('Programa Encerrado')
        print('-=' * 30)
        print(f'Foram cadastrados {contador18} Pessoa(s) com mais de 18 anos')
        print(f'Foram cadastrados {sexoh} Homem(s)')
        print(f'Foram cadastradas {contador} Mulher(es) com menos de 20 anos')
        print('-=' * 30)
        break