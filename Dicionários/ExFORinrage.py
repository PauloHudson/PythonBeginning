estado = {}
brasil = []
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Silga: '))
    brasil.append(estado.copy())
    #preciso criar a cópia, para que não de erro e só de append
    #no primeiro valor é igual ao fatiamento [:]
for e in brasil: #para cada estado em brasil
    for k in brasil.values():
        print(f'Estado de {k}')