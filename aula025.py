""" 
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caracter)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= Força o número a aparecer antes dos zeros
Sinal - + ou -
ex.:0>-100,.1f
conversion flags - !r !s !a
 """

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')

print(f'{1000.939218391239812:0=+10,.1f}')
print(f'{1000.939218391239812:0=+10,.1f}')
print(f'O Hexadecimal de 1500 é {1500:08X}')

print(f'{variavel}')
