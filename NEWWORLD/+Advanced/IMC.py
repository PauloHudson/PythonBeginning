print('Calculador de IMC')
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / altura**2
if imc <= 18.5:
    print(f'Abaixo do Peso {imc:.4}')
elif imc <= 25:
    print(f'Peso Ideal {imc:.4}')
elif imc <= 30:
    print(f'Sobrepeso {imc:.4}')
elif imc <= 40:
    print(f'Obesidade {imc:.4}')
else:
    print(f'Obesidade-Morbida {imc:.4}')