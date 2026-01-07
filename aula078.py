""" Manipulando chaves e valores em dicionários """



chave = 'nome'
pessoa = {}

pessoa['nome'] = 'Esdras Abdir'
pessoa['sobrenome'] = 'Oliveira'
pessoa[chave] = 'Maria'
del pessoa['sobrenome']
print(pessoa)

if pessoa.get('sobrenome', None) is None:
        print('Não existe')
else: 
        print(pessoa['sobrenome'])

# print(pessoa.get('sobrenome'))
