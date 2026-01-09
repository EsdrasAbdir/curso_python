# raise - lançando exceções (erros)

# print(123)

# raise ValueError('Deu erro')


def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por 0')
    return True


def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (int,float)):
        raise TypeError( 
        f'"{n}" deve ser int ou float.'
        f'"{tipo_n.__name__}" enviado.'
        )
    
    return True

def division(n,d):
    deve_ser_int_ou_float(n)
    nao_aceito_zero(d)

    return n/d

print(division('e',2))