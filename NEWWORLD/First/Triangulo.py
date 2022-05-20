a = int(input('Digite o Primeiro Valor:'))
b = int(input('Digite o Segundo Valor:'))
c = int(input('Digite o Terceiro Valor:'))
if ((b - c) < a) and (a < b + c) or ((a - c) < b) and (b < a + c) or ((a - b) < c) and (c < a + b):
    print('é possível formar um triângulo!')
else:
    print('não é possível formar um triângulo!')
