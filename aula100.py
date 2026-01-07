# dir, hasattr e getattr em Python

string = 'Esdras'
metodo = 'upper'

if hasattr(string, metodo ):
    print('Existe upper')
    print(getattr(string, metodo)())


