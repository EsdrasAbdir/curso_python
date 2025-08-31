""" 
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ['Esdras','Anne'] 
# lista_b = lista_a.copy()
lista_b = lista_a
lista_a[0] = 'Qualquer coisa'
# print(id(lista_a))
print(lista_a)
print(lista_b)
