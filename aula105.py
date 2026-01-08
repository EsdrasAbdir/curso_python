# Try , except, else e finally


try:
    a = 18
    b = 0
    # print(b[0])
    print('Linha 1'[1000])
    c = a/b
except ZeroDivisionError:
    print('Dividiu por zero')

except NameError:
    print('Nome não está definido')

except (TypeError,IndexError):
    print('TypeError + IndexError')

except Exception:
    print('ERRO DESCONHECIDO')

print('CONTINUAR')