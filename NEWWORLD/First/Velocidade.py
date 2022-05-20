velocidade = int(input('Digite a velocidade do veículo: '))
if velocidade >= 80:
    multa = (velocidade - 80)* 7
    excesso = velocidade - 80
    print('Você foi multado em {}, correspondente a 7R$ a cada Km excedente ({}Kms multados.)'.format(multa, excesso))
else: 
    print('velocidade compatível com a segurança, parabéns!!')
print('------FIM------')