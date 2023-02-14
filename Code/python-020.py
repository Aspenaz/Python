""" Docstrings """


# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================
# Documentando el código

def area_trapecio(BaseMayor, BaseMenor, Altura):
    '''area_trapecio: Calcula el área de un trapecio.
    area_trapecio = (BaseMayor + BaseMenor) * Altura / 2'''
    return (BaseMayor + BaseMenor) * Altura / 2

print(area_trapecio(100, 40, 40))  #  28
print()

print(area_trapecio.__doc__)
print()

print(help(area_trapecio))

# ===========================================================
print('\n' + '=' * 94 + '\n')
# ===========================================================



