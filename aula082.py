# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

print(perguntas[0].get('Pergunta'))

for opcao in perguntas[0].get('Opções'):
    print(f'Opção',opcao)
resposta = input('Digite o número da opção : ')
resposta_correta = int(resposta)

if resposta_correta  == 4:
    print('Você acertou a primeira questão 👍')
else:
    print('Você errou a primeira questão ❌')

...

print(perguntas[1].get('Pergunta'))

for opcao in perguntas[1].get('Opções'):
    print(f'Opção',opcao)
resposta_1= input('Digite o número da opção : ')
resposta_correta_1 = int(resposta_1)
if resposta_correta_1  == 25:
    print('Você acertou a segunda questão👍')
else:
    print('Você errou a segunda questão ❌')


print(perguntas[2].get('Pergunta'))

for opcao in perguntas[2].get('Opções'):
    print(f'Opção',opcao)
resposta_2 = input('Digite o número da opção : ')
resposta_correta_2 = int(resposta_2)

if resposta_correta_2 == 5:
    print('Você acertou a terceira questão 👍')
else:
    print('Você errou a terceira questão ❌')




