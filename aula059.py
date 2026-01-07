""" 
Faça uma lista de compra com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista_de_compra = []
item_adicionado = ''
while True:
    print('Selecione uma opção:')
    entrada = input('[i]nserir [a]pagar [l]istar : ')
    if entrada == 'i':
        item_adicionado = input('Digite um item para colocar na lista : ')
        print(item_adicionado)
        lista_de_compra.append(item_adicionado)
    elif entrada == 'a':
        numero_str = input('Digite o índice a ser excluído: ')
        try:
            numero = int(numero_str)
            lista_de_compra.pop(numero)
        except ValueError:
            print('Por favor digite número inteiro. ')
        except IndexError:
            print('Índice não existe na lista')
    elif entrada == 'l':
       if not lista_de_compra:
           print('Não tem itens a ser removido.')
       else:
           for indice, item in enumerate(lista_de_compra):
            print(indice,item)      
    else:
        print('Letra inválida')
        

        
   
