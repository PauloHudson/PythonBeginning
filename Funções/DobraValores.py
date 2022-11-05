def dobra(lst): #esse LST pode ser chamado de qualquer coisa
    pos = 0
    while pos < len(lst): #enquanto for menor que o tamanho da lista. 
        lst[pos] *= 2 #Dobrar
        pos = pos + 1

valores = [1, 4, 3, 2, 1, 5, 7, 4, 2]
dobra(valores)
print(valores)