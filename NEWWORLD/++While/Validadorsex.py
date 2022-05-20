#valide se o sexo da pessoa é masculino ou femino

sexo = 'm' or 'f'
while sexo == 'm' or 'f' :
    sexo=str(input('Digite uma opção sexual: [m/f]'))
    if sexo != 'm':
        if sexo != 'f':
            print('Digite novamente, opção invalida!')