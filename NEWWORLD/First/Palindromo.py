word = input('Digite um palavra: ').upper().replace(" ", "")
if word == word[::-1]:
   print('Palíndromo')
else:
    print('Não é palíndromo')