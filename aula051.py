""" 
Método úteis:
.....append - Adiciona um item ao final
.....insert - Adiciona um item no índice escolhido
.....pop - apaga um índice
.....clear - limpa a lista
.....extend - estende a lista
.....+ -   - contana listas
"""

lista = [10, 20, 30, 40]
lista.append('Esdras')
lista.append(1233)
import os
os.system('cls')
del lista[-1]
# lista.clear()
lista.insert(0, 5)
print(lista)