#5 - Escreva um programa para calcular a redução do tempo de viwadda de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias:
print ('Olá Fumante, Antes de Começarmos saiba que isso se aplica a todo tipo de fumo, viu, não apenas cigarro, mas por fins educativos estaremos tratando de maços fumados por dia :D')
dia = int(input('Quantos cigarros você fuma por dia? '))
anos = int(input('A Quantos Anos VC Fuma? '))
cigarros = int(dia * 365) * anos
#12 representa a quantidades de cigarros dentro de um maço
#aqui eu sei quantos cigarros ele fumou durante a vida
#se a cada 1 cigarro ele perde 10 minutos (equação é 10 * x dias / anos)
lifetime = int((cigarros * 10) / 1440)
anos = float(lifetime / 365)
#1440 e a quantidade de minutos por dia
#life time eu sei quantas horas ao total ele perdeu fumando

print (f'vc fumou {cigarros} cigarros durante a vida')
print (f'equivalente a perder cerca de {lifetime} dias de vida ou {anos} anos ')
