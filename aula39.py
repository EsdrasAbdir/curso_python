""" 
Iterando strings com while
"""
#       01234567891011
nome = 'Esdras Abdir' #Iteráveis
tamanho_nome =  print(len(nome))
nova_string = '*E*s*d*r*a*s *A*b*d*i*r'

indice=0
novo_nome = ''
while indice < len(nome):
    letra = (nome[indice])
    novo_nome += f'*{letra}'
    indice += 1
novo_nome += '*'
print(novo_nome)



            
