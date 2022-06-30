test = list()
test.append('gustavo')
test.append(49)
galera = list()
galera.append(test[:])
test[0] = 'maria'
test[1] = 22
galera.append(test[:])
print(galera)