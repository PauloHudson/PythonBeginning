
i = 0
while True:
    print('-'* 24)
    a = int(input('Deseja a Tabuada do ? '))
    print('-'* 24)
    if a > 0:
     for i in range (1, 11):
        print(f'{a} X {i} = {i * a}')
        i = i + 1
    if a < 0:
        print('Valor Não Existente, Tente Novamente com valor POSITIVO!')
        break
   
