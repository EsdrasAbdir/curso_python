""" Desempacotamento em chamadas
de métodos e funções
"""
string = 'ABCD'

lista = ['Maria','Helena',1,2,3,'Eduarda']

tupla = 'Python', 'é', 'legal'

salas =[ 
#.........0.........1
    ['Maria', 'Helena', ], # 0
#.........0
    ['Elaine',], # 1
#.........0......1............2.......3
    ['Luiz', 'João', 'Eduarda',('Thomas','Ricardo','Lopes','henrique') ], #2
#...............................0............1........2........3.......
]

# a,b,*_ ,u= lista
# print(a,u)

# for nome in lista:
#     print(nome, end = ' ')
# print(*lista)
# print(*string)

print(*salas, sep='\n')