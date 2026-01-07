""" 
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# texto = iter('Luiz') # __iter__()

# print(next(texto)) # __next__()
# print(next(texto)) # __next__()
# print(next(texto)) # __next__()
# print(next(texto)) # __next__()

texto = 'Luiz' # Iterável
# iterador = iter(texto) #Iterador

# while True:
#     try:
#         print(next(iterador))
#     except StopIteration:
#         break

for letra in texto:
    print(letra)


