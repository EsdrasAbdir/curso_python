"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
#Contagem regressiva do primeiro dígito

import sys

cpf_enviado_usuario = '746.824.890-70'\
    .replace('.','') \
    .replace('-','') \
    .replace(' ','') 


cpf_enviado_usuario_e_sequencial = cpf_enviado_usuario == cpf_enviado_usuario[0] * len(cpf_enviado_usuario)

if cpf_enviado_usuario_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()


nove_primeiro_digitos = cpf_enviado_usuario[:9]

contador_regressivo = 10

resultado = 0
for numero in nove_primeiro_digitos:
    resultado += int(numero) * contador_regressivo
    contador_regressivo -= 1    

segundo_resultado = resultado * 10


terceiro_resultado = segundo_resultado % 11


avaliador = (terceiro_resultado if terceiro_resultado <=9 else 0)


# segundo digíto do cpf

novo_digito = cpf_enviado_usuario[:10]
contador_regressivo_2 = 11
resultado_2 = 0

for digito in novo_digito:
    resultado_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
print(resultado_2)

resultado_2 = resultado_2 * 10
resultado_2 = resultado_2 % 11

0 if resultado_2 > 9 else resultado_2
print(resultado_2)


cpf_gerado_pelo_calculo = f'{nove_primeiro_digitos}{avaliador}{resultado_2}'

print(cpf_gerado_pelo_calculo)


if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print('CPF válido')
else: 
    print('CPF inválido')






