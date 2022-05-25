#valide se o sexo da pessoa é masculino ou femino
digitar = 'S' or 'M'
while digitar != 'F' or 'M':
   digitar = str(input('Digite apenas [M, F]: ')).upper()
   if digitar == 'F':
      print('Feminino')
   elif digitar == 'M':
      print('Masculino')
