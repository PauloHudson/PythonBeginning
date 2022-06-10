contador = soma = 0
print('QUANDO QUISER PARAR DIGITE 999')
while True:
    numero = int(input('Digite um Valor: '))
    if numero == 999:
        print(f'a soma dos {contador} valores doi de {soma}')
        break
    soma = soma + numero
    contador = numero + 1
