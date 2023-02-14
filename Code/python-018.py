""" Funciones que imponen nombrar o no parámetros """


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================
""" Modos habituales de llamar a una función (por referencia posicional o por nombre): """

def funcion1(x, y, z):
    return x + y + z

print(funcion1(1, 2, 3))        # 6
print(funcion1(x=1, y=2, z=3))  # 6
print(funcion1(z=3, x=1, y=2))  # 6


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================
""" los parámetros a la izquierda de la barra '/' deben indicarse sin nombrar.
Si no es así se producirá una excepción de tipo TypeError: """


def funcion2(x, y, z, /):
    return x + y + z

print(funcion2(1, 2, 3))        # 6 (llamada correcta)
# print(funcion2(x=1, y=2, z=3))  # TypeError: funcion2() got some positional-only arguments passed as keyword arguments: 'x, y, z'


print()


""" 'x' por estar a la izquierda de la barra '/' necesariamente debe indicarse sin nombrar: """
def funcion3(x, /, y, z):   
    return x + y + z

# print(funcion3(x=1, y=2, z=3))  # TypeError: funcion3() got some positional-only arguments passed as keyword arguments: 'x'
print(funcion3(1, z=2, y=3))


# ===========================================================
# print('\n' + '=' * 94 + '\n')
# ===========================================================
""" Un asterisco '*' entre los parámetros impone que todos los que se
encuentren a su derecha tengan que referenciar su nombre: """

def funcion4(x, y, *, z):
    return x + y + z

print(funcion4(1, 2, z=3)) # 6
print(funcion4(x=1, y=2, z=3)) # 6 (es correcta esta llamada)
print(funcion4(1, 2, 3)) # TypeError: funcion4() takes 2 positional arguments but 3 were given


# ===========================================================
# print('\n' + '=' * 94 + '\n')
# ===========================================================


# ===========================================================
# print('\n' + '=' * 94 + '\n')
# ===========================================================


