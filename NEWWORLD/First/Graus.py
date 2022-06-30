#4 - Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32. 8) Faça agora o contrário, de Fahrenheit para Celsius.
print('=-='*30)
escolha = input('Deseja Converter em Fahrenheit or Celsius? [F or C]: ').upper()
print('=-='*30)
while True:
    if escolha == 'C':
        c = int(input('Digite a Temperatura em graus a ser convertida: '))
        conversao = int(c * (9/5) + 32)
        print (f' {c} Graus (Celsius) em Fahrenheit equivale a {conversao}°F')
        deseja = input('Deseja Fazer Outra Conversão [S or N]?').upper()
        if deseja == 'S':
          escolha = input('Deseja Converter em Fahrenheit or Celsius? [F or C]: ').upper()
        if deseja == 'N':
            break
    elif escolha == 'F':
        f = int(input('Digite a Temperatura em graus °F a ser convertida: '))
        conversaox = int((f - 32) * 5/9)
        print (f' {f} Graus (Fahreint) em Celcius equivale a {conversaox}°C')
        deseja = input('Deseja Fazer Outra Conversão [S or N]?').upper()
        if deseja == 'S':
          escolha = input('Deseja Converter em Fahrenheit or Celsius? [F or C]: ').upper()
        if deseja == 'N':
            break
    else:
        print('Escolha Somente entre [F or C]')
        escolha = input('Deseja Converter em Fahrenheit or Celsius? [F or C]: ').upper()
    
