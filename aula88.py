# Exemplo de uso dos sets

letras= set()
while True:
    letra = input('Digite a letra secreta: ')
    letras.add(letra)
    if 'l' in letras:
        print('Parabéns, você descobriu a letra secreta 😁 ')
        break
    print(letras)


