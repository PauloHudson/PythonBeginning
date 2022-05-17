print('FEDERAÇÃO DE NATAÇÃO PAULO HUDSON')
print('PRECISAMOS SABER QUAL A SUA IDADE PARA ADEQUAR CORRETAMENTE A COMPETIÇÃO')
ano = int(input('DIGITE O ANO DE NASCIMENTO:'))
idade = (2022 - ano)
if idade < 9:
    print('MIRIM')
elif idade >= 9 and idade <= 14:
    print('INFANTIL')
elif idade <= 18:
    print('JUNIOR')
elif idade < 20:
    print('SENIOR')
else:
    print('MASTER, VELHOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')