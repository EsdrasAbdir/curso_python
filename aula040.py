""" 
Calculadora com while 
"""

while True:
    numero_1 = float(input('Digite um número: '))
    numero_2 = float(input('Digite outro número: '))
    operador = input('Digite o operador (+-/*): ')
    if operador == '+':
        soma = numero_1 + numero_2
        print(soma)
    elif operador == '-':
        menos = numero_1 - numero_2
        print(menos)
        print(menos)
    elif operador == '/':
        divisao = numero_1 / numero_2
        print(divisao)
    else:
        multiplicacao = numero_1 * numero_2
        print(multiplicacao)
    
    #########
    sair = input('Deseja [s]air: ').lower().startswith('s')
    print(sair)
    if sair is True:
        break
