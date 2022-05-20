sexo = str(input('Digite seu sexo [F, M]:')).upper()
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite somente [F, M]:')).upper()
if sexo == 'F':
    print('Feminino')
elif sexo == 'M':
    print('Masculino')
    