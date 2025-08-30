""" 
listas em Python
tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimento reutilizáveis - índice e fatiamento
Métodos úteis
......append , insert, pop , del, clear , extend, +
Create Read Update ... Delete
Criar, ler , alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
import os
os.system('cls')
# del lista[2]
# print(lista)
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'removido' , ultimo_valor)