#a = float(input('escreva um numero: '))
#b = float(input('escreva outro numero: '))
#c = float(input('mais um corno: '))
#x = (a + b - c)
#print (x)
lista = []
for c in range(0,3):
    lista.append(int(input('Digite um valor: ')))
print(f'{lista[0]} + {lista[1]} - {lista[2]} = {lista[0] + lista[1] - lista[2]}')