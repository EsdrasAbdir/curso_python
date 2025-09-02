""" Lista de listas e seus índices """

salas =[ 
#.........0.........1
    ['Maria', 'Helena', ], # 0
#.........0
    ['Elaine',], # 1
#.........0......1............2.......3
    ['Luiz', 'João', 'Eduarda',('Thomas','Ricardo','Lopes','henrique') ], #2
#...............................0............1........2........3.......
]

# print(salas[0][1]) # i = 'Helena'
# print(salas[2][2]) # i = 'Eduarda'
# print(salas[2][3][2]) # i = 'Lopes'

for sala in salas:
    for aluno in sala:
        print(aluno)