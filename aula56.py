""" Introdução ao desempacotamento """

nomes = ['Maria', 'Helena', 'Luiz']

# nome1, nome2, nome3 = nomes

# print(nome2)

_  ,nome2, *_ = ['Maria', 'Helena', 'Luiz']
print(nome2,_)