""" 
Exercícios com funções

Crie uma função que multiplique todos os argumentos
não nomeados recebidos.
retorne o total para uma variável e mostre o valor
da variavel.
crie um função que fala se um número é par ou ímpar.
retorne se o número é par ou ímpar
"""

# Primeira tarefa
total = 1
def multiplica (*args):
    global total
    for numero in args:
        total *= numero
    return total

variavel = multiplica(1,2,3,4)

print(variavel)


#Segunda tarefa
# numero = 4

# def par_impar():
#     return 'O número é par!' if numero % 2 == 0 else 'Número é ímpar!'  


# print(par_impar())

    