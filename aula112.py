import importlib


import aula112_m

print(aula112_m.variavel)

for i in range(10):
    print(i)
    import aula112_m # Singleton - só existe uma instância dele salvo na memória(eficiência)
    importlib.reload(aula112_m)

print('fim')