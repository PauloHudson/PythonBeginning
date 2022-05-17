i = 0
for a in range(1, 7):
    a = int(input('Digite um número: '))
    if a % 2 == 0:
        i = i + a
    else:
        print('Este não é um número par, não havera soma')
print (f'A soma foi apenas realizada entre os pares = {i}')


