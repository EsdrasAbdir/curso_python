""" 
Exercícios
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como pârametro
"""

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))



# Outro modo de se fazer:
# def duplica(numero):
#     return numero * 2

# def triplica(numero):
#     return numero * 3

# def quadruplica(numero):
#     return numero * 4




# print((duplica(2)))
# print((triplica(2)))
# print((quadruplica(2)))