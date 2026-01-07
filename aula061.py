""" 
split e join com list e str
split - divide uma string
join - une uma string
"""
import os

frase = 'Olha só que ,  coisa interessante'
lista_frases_cruas = frase.split(',')

lista_frase_corrigida = []
os.system('cls')
print(lista_frases_cruas)

for i, frase in enumerate(lista_frases_cruas):
   lista_frase_corrigida.append(lista_frases_cruas[i].strip())

print(lista_frase_corrigida)

frases_unidas = ', '.join(lista_frase_corrigida)
print(frases_unidas)