""" 
funções decoradoras e decoradores
Decorar = Adicionar/ Remover / Restringir / Alterar
funções decoradoras são funções que decoram outras funções
decoradores são usados para fazer o python
usar as funções decoradoras em outras funções.
decoradores são "Syntax Sugar" (Áçucar sintático)
"""

def e_string(param):
    if not isinstance(param,str):
        raise TypeError("param deve ser string")


def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args,**kwargs)
        print(f'O seu resultado foi {resultado}')
        print('Ok, você foi decorado')
        return resultado
    return interna

@criar_funcao
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]



invertida = inverte_string('123')

print(invertida)
