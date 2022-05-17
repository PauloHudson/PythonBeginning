#4 - Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32. 8) Faça agora o contrário, de Fahrenheit para Celsius.
c = int(input('Digite a Temperatura em graus a ser convertida: '))
conversao = int(c * (9/5) + 32)
print (f' {c} Graus (Celsius) em Fahrenheit equivale a {conversao}°F')

f = int(input('Digite a Temperatura em graus a ser convertida: '))
conversaox = int((f - 32) * 5/9)
print (f' {f} Graus (Fahreint) em Celcius equivale a {conversaox}°C')

