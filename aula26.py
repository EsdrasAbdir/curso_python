""" 
Fatiamento de strings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]
obs.: a funcao len retorna a qtd
de caracteres da str
 """
variavel = 'Olá mundo'
(print(len(f'{variavel}')))
print(f'{variavel[2]}')

print(variavel[-8:-2])

print(f'{variavel[::-1]}')