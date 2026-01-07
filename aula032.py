""" 
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número 
inteiro, informe que não é um número inteiro
"""
try:
    numero = int(input('Digite um número inteiro:'))
    if numero % 2 ==0:
        print('Esse número é par')
    else:
        print('Esse número é ímpar')
except ValueError:
    print('Não é um número inteiro')

""" 
Faça um programa que pergunte a hora ao usuário e, basenando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""
try:
    horario = int(input('Digite o horário de 0 a 24: '))
    if horario <= 11:
        print('Bom dia')
    elif horario <= 17:
        print('Boa tarde')
    else:
        print('Boa noite')
except ValueError:
    print('Não foi digitado um horário válido.') 

""" 
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal";
maior que 6 escreva "Seu nome é muito grande."
"""


nome = input('Digite seu nome: ')
if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')


