distancia = int(input('Digite a distância Percorrida: '))
if distancia <= 200:
    valor = (distancia * 0.5)
    print('o valor a ser pago sera de {}R$, sendo percorridos {}Km (custo de 0.5R$ por Km).'.format(valor, distancia))
else:
    valorx = (distancia * 0.45)
    print('o valor a ser pago sera de {}R$, sendo percorridos {}Km (custo de 0.45R$ por km).'.format(valorx, distancia))
print('-----Fim----')