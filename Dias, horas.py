#1 - Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos
a = int(input('Digite a Sua data de Nascimento: '))
b = int(2022 - a)
c = int(b * 365)
d = int(c * 1440)
e = int(c * 24)
f = int (c * 86400)
#print (f'{b} Anos')
#print (f'{c} Dias')
#print (f'{d} Minutos')
#print (f'{e} Horas')
#print (f'{f} segundos')

print(f'Para uma pessoa Nascida em {a} Ela/Ele Possui {b} Anos, {c} Dias, {e} Horas, {d} Minutos e {f} Segundos de Vida.')