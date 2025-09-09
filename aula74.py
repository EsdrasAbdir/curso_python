""" 
Higher Order Functions
"""

def saudacao(msg,nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)



print (
    executa(saudacao, 'Bom dia','Esdras')
)

# print(saudacao('Bom dia'))