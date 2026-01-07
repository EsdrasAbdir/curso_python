""" 
Calculadora com while mais robusta
"""

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um operador (+-/*): ')

    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos or len(operador) > 1:
        print('Operador inválido')
        continue

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
    except ValueError:
            print('Número inválido')
            continue
        ###
    if operador == '+':
        soma = num_1_float + num_2_float
        print(soma)
    elif operador == '-':
        subtracao = num_1_float - num_2_float
        print(subtracao)
    elif operador == '/':
        divisao = num_1_float / num_2_float
        print(divisao)
    else:
        multiplicacao = num_1_float * num_2_float
        print(multiplicacao)

    sair = input('Quer sair? [s]im?' ).lower().startswith('s')
    if sair == True:
        break