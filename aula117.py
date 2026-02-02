""" 
funções decoradoras e decoradores
Decorar = Adicionar/ Remover / Restringir / Alterar
funções decoradoras são funções que decoram outras funções
decoradores são usados para fazer o python
usar as funções decoradoras em outras funções.
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
        print('Ok, você foi decorado')
        return resultado
    return interna

def inverte_string(string):
    return string[::-1]


inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('123')

print(invertida)
