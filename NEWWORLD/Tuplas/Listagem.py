

lista = ('Hamburguer', 2.0, 'Água', 3.0, 'Sorvete', 5.0, 'Pastel', 10.3, 'Coração de Galinha', 20.5,  
        'Farinha', 5.0, 'Refrigerante', 7.5)
            
print('=-=' * 21)
a = ('LISTAGEM DE PRODUTOS')
print(a.center(60))
print('=-=' * 21)
for i in range(0, len(lista), 2):
    print(f'{lista[i]:.<55} R$ {lista[i+1]:>4}')
print('=-=' * 21)
    
